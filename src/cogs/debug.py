import discord
from data import *
from baseCommandModule import BaseCommandModule
from discord.ext import commands
from utilities import Table
from utilities.diagnostics import verboseError
from utilities.diagnostics import benchmark
import aiohttp    
import io
import os
import platform
import datetime
from utilities import images
from utilities import Embed

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
    @verboseError
    @executionTime()
    async def t4(self, ctx, prop: int):
        await ctx.send(f"t4  prop: {prop}")

    @t4.error
    async def t4_error(*args):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(error)

    @commands.command()
    @verboseError
    @benchmark
    async def t5(self, ctx):
        """Tests a crapy embed"""
        embed = Embed()
        embed.setTitleDesc("test title","this is a test description")
        await embed.setThumbnailUrl(ctx,self.bot)
        
def setup(bot):
    bot.add_cog(Debug(bot))
