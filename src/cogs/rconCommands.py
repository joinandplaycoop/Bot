import discord
import asyncio
from discord.ext import commands
from utilities.diagnostics import handle_aio_exceptions, verboseError, benchmark
from models import Server
from utilities import handlers
from utilities.rcon import RconConnection
from baseCommandModule import BaseCommandModule
import time
from config import Config

class RconCommands(BaseCommandModule):
    """description of class"""

    def __init__(self, bot):
         self.bot = bot
         self._tasks = None
    
    @commands.command()
    async def players(self, ctx, param=""):
        await start_background_tasks(ctx,"/players", handlers.handle_players)
        
 
async def start_background_tasks(ctx, command: str, handler):

    coroutines = []
    for s in Config.cfg.servers:
        coroutines.append(poll_rcon(s, command, handler, ctx))

    #coroutines = [poll_rcon(s.serverName,command, handler, ctx),
        #Calls to other servers here
        #poll_rcon('/admins', handlers.handle_admins),
        #poll_local_mods(handlers.handle_mods),
        #poll_config(handlers.handle_config),
        #determine_ip(handlers.handle_ip),
        #poll_mod_database(handlers.handle_mod_database),
    #]

    _tasks = asyncio.gather(*map(handle_aio_exceptions, coroutines))

async def start_background_task(server: Server, ctx, command: str, handler):
    coroutines = [poll_rcon(server, command, handler, ctx)]
    _tasks = asyncio.gather(*map(handle_aio_exceptions, coroutines))

async def poll_rcon(server, command: str, handler, ctx, interval=1):
    """More specific version of monitor_coroutine() for rcon commands"""
    
    start = time.time()
    async with RconConnection(server, ctx) as rcon:
        previous_value = None
        #while True:
        try:
            value = await rcon.run_command(command)
            if value != previous_value:
                await handler(ctx, server, value)
                end = time.time()
                print(f"poll_rcon() [{server.serverName}] [{command}]: {end - start}")
            previous_value = value
            #await asyncio.sleep(interval)
        except asyncio.CancelledError:
            return


#async def poll_config(handler, interval=10):
#    """Execute the config command multiple times in order to get all config options"""
#    logger.info('Setting up monitor: Server config polling (via RCON)')
#    options = ['afk-auto-kick', 'allow-commands', 'autosave-interval', 'autosave-only-on-server',
#               'ignore-player-limit-for-returning-players', 'max-players', 'max-upload-speed', 'only-admins-can-pause',
#               'password', 'require-user-verification', 'visibility-lan', 'visibility-public']
#    async with RconConnection() as rcon:
#        previous_config = None
#        while True:
#            try:
#                server_config = {}
#                for option in options:
#                    server_config[option] = await rcon.run_command('/config get {}'.format(option))

#                if server_config != previous_config:
#                    handler(server_config)
#                previous_config = server_config.copy()
#                await asyncio.sleep(interval)
#            except asyncio.CancelledError:
#                return


def setup(bot):
    bot.add_cog(RconCommands(bot))
