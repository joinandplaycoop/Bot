import discord
import asyncio
from data import *
from baseCommandModule import BaseCommandModule
from discord.ext import commands
from utilities.diagnostics import verboseError, benchmark
import aiohttp    
import io
import os
import platform
import datetime
from utilities import images, Embed,Table
from config import Config
from cogs.factorioConfig import start_background_task,start_background_tasks

#if os.name == 'nt': # Windows
#    basePath = 'C:\\working\\'
#else:
#    basePath = '/working/'

#print(f"{platform.uname()} basePath = '{basePath}'")
class Debug(BaseCommandModule):
    """Cog of Debug commands"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def t1(self, ctx):
        try:
            result = PlayersOnline_Result.execute(self._session)

            #for row in result:
            table = Table("Server","Online")

            for r in result:
                table.addRow(r.FKServerId, r.TotalPlayersOnline)

            await ctx.send(table.toString())
        except Exception as e:
            await ctx.send(str(e))

    @commands.command()
    @verboseError
    async def t2(self, ctx):
        try:
            command = os.popen('ls -al')
            cmd = command.read()
            print(cmd)
            if len(cmd) > 0:
                await ctx.send(cmd)
            c = command.close()
            print(c)
            #await ctx.send(command.close())
            await ctx.send("Check screen -x")
        except Exception as e:
            await ctx.send(str(e))


    @commands.command()
    @verboseError
    async def t3(self, ctx, daysAgo:int):
        """ '''test''' """
        msg = await ctx.send("getting file")

        buffer = await images.getRockets(daysAgo)

        await ctx.send(file = discord.File(buffer,"stat.png")) 
        await msg.delete()

       
    @commands.command()
    async def rc(self, ctx, *args):
        rcCommand = ' '.join(map(str, args))
        await start_background_tasks(ctx, rcCommand, handle_dynamic)
        #self._dynTask = asyncio.create_task(poll_rcon(rcCommand,
        #handle_dynamic, ctx))

    @commands.command()
    async def rcs(self, ctx, serverName, *args):
        s = next((x for x in Config.cfg.servers if x.serverName == serverName), None)
        if s == None:
            return await ctx.send(f"No server named `{serverName}`")

        rcCommand = ' '.join(map(str, args))
        
        await start_background_task(s, ctx,rcCommand, handle_dynamic,)
        #self._dynTask = asyncio.create_task(poll_rcon(rcCommand,
        #handle_dynamic, ctx))

    @commands.command()
    @verboseError
    @benchmark
    async def t5(self, ctx):
        """Tests a crapy embed"""
        embed = Embed()
        embed.setTitleDesc("test title","this is a test description")
        await embed.setThumbnailUrl(ctx,self.bot)
        
async def  handle_dynamic(ctx, server, data:str):
    await ctx.send(data)

def setup(bot):
    bot.add_cog(Debug(bot))
