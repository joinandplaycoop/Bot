import asyncio
import socket
import struct
import sys
from config import Config, Server
import logging


MESSAGE_TYPE_AUTH = 3
MESSAGE_TYPE_AUTH_RESP = 2
MESSAGE_TYPE_COMMAND = 2
MESSAGE_TYPE_RESP = 0
MESSAGE_ID = 0

logger = logging.getLogger(__name__)


class RconConnectionError(Exception): pass
class RconTimeoutError(Exception): pass
class RconAuthenticatedFailed(Exception): pass


async def send_message(writer, command_string, message_type):
    """Packages up a command string into a message and sends it"""
    logger.debug('Send message to RCON server: {}'.format(command_string))

    try:
        # size of message in bytes:
        # id=4 + type=4 + body=variable + null terminator=2 (1 for python
        # string and 1 for message terminator)
        message_size = (4 + 4 + len(command_string) + 2)
        message_format = ''.join(['=lll', str(len(command_string)), 's2s'])
        packed_message = struct.pack(message_format, message_size, MESSAGE_ID, message_type, command_string.encode('utf8'), b'\x00\x00')
        writer.write(packed_message)
        response_data = await asyncio.wait_for(writer.drain(),
            timeout=Config.cfg.rconTimeout)

    except asyncio.TimeoutError:
        raise RconTimeoutError('Timeout sending RCON message. type={}, command={}'.format(message_type, command_string))


async def get_response(reader):
    """Gets the message response to a sent command and unpackages it"""
    response_id = -1
    response_type = -1
    try:
        response_size, = struct.unpack('=l', await reader.read(4))
        message_format = ''.join(['=ll', str(response_size - 9), 's1s'])

        response_data = await asyncio.wait_for(reader.read(response_size),
            timeout=Config.cfg.rconTimeout)
        response_id, response_type, response_string, response_dummy = struct.unpack(message_format, response_data)
        response_string = response_string.rstrip(b'\x00\n')
        return response_string, response_id, response_type

    except asyncio.TimeoutError:
        raise RconTimeoutError('Timeout receiving RCON response')


class RconConnection():

    def __init__(self, server: Server, ctx):
         self.server = server
         self.ctx = ctx

    async def __aenter__(self):
        logger.debug('Authenticating with RCON server {}:{} using password "{}"'.format(self.server.rcon.host,
            self.server.rcon.port,
            self.server.rcon.password,))

        try:
            self.reader, self.writer = await asyncio.wait_for(asyncio.open_connection(self.server.rcon.host, self.server.rcon.port),
                timeout=Config.cfg.rconTimeout)
        except asyncio.TimeoutError:
            e = 'Timeout connecting to RCON server {}:{}'.format(self.server.rcon.host, self.server.rcon.port)
            await self.ctx.send(f"[{self.server.serverName}] - Timeout connecting to RCON")
            raise RconTimeoutError(e)
        except ConnectionRefusedError:
            e = 'Server {} refused attempted RCON connection on port {}'.format(self.server.rcon.host, self.server.rcon.port)
            await self.ctx.send(f"[{self.server.serverName}] - Connection Refused Error")
            raise RconConnectionError(e)

        await send_message(self.writer, self.server.rcon.password, MESSAGE_TYPE_AUTH)
        response_string, response_id, response_type = await get_response(self.reader)

        if response_id == -1:
            e = 'Failed to authenticate with RCON server {}:{} using password "{}"'.format(self.server.rcon.host,
                self.server.rcon.port,
                self.server.rcon.password)
            await self.ctx.send(f"[{self.server.serverName}] - Failed to authenticate with RCON server")
            raise RconAuthenticatedFailed()
        else:
            logger.debug('Successfully authenticated with RCON server')

        return self

    async def __aexit__(self, exc_type, exc, tb):
        self.writer.close()

    async def run_command(self, command: str):
        logger.debug('Running RCON command: {}'.format(command))

        await send_message(self.writer, command, MESSAGE_TYPE_COMMAND)
        response_string, response_id, response_type = await get_response(self.reader)

        # See:
        # https://developer.valvesoftware.com/wiki/Source_RCON_Protocol#Multiple-packet_Responses
        # Basically we get an empty packet after each response
        if command.startswith('/config'):
            # ServerConfig commands seem to be multi-packet responses
            await get_response(self.reader)

        return response_string

