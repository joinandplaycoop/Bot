import discord
import asyncio
from discord.ext import commands
from utilities.diagnostics import handle_aio_exceptions
from utilities.diagnostics import verboseError
from utilities.diagnostics import benchmark
from utilities import handlers
from utilities.rcon import RconConnection
from baseCommandModule import BaseCommandModule

class FactorioConfig(BaseCommandModule):
    """description of class"""

    def __init__(self, bot):
         self.bot = bot
         self._tasks = None
    
    @commands.command()
    @verboseError
    @benchmark
    async def players(self, ctx, param=""):
        await self.start_background_tasks(ctx)


    async def start_background_tasks(self,ctx):
        coroutines = [
            poll_rcon('/players', handlers.handle_players, ctx),
            #poll_rcon('/admins', handlers.handle_admins),
            #poll_local_mods(handlers.handle_mods),
            #poll_config(handlers.handle_config),
            #determine_ip(handlers.handle_ip),
            #poll_mod_database(handlers.handle_mod_database),
        ]

        self._tasks = asyncio.gather(
            *map(handle_aio_exceptions, coroutines)
        )

async def poll_rcon(command, handler, ctx, interval=1):
    """More specific version of monitor_coroutine() for rcon commands"""
    async with RconConnection() as rcon:
        previous_value = None
        while True:
            try:
                value = await rcon.run_command(command)
                if value != previous_value:
                    await handler(ctx, value)
                previous_value = value
                await asyncio.sleep(interval)
            except asyncio.CancelledError:
                return


async def poll_config(handler, interval=10):
    """Execute the config command multiple times in order to get all config options"""
    logger.info('Setting up monitor: Server config polling (via RCON)')
    options = ['afk-auto-kick', 'allow-commands', 'autosave-interval', 'autosave-only-on-server',
               'ignore-player-limit-for-returning-players', 'max-players', 'max-upload-speed', 'only-admins-can-pause',
               'password', 'require-user-verification', 'visibility-lan', 'visibility-public']
    async with RconConnection() as rcon:
        previous_config = None
        while True:
            try:
                server_config = {}
                for option in options:
                    server_config[option] = await rcon.run_command('/config get {}'.format(option))

                if server_config != previous_config:
                    handler(server_config)
                previous_config = server_config.copy()
                await asyncio.sleep(interval)
            except asyncio.CancelledError:
                return


def setup(bot):
    bot.add_cog(FactorioConfig(bot))
