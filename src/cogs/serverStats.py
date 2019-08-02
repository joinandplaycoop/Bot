from baseCommandModule import BaseCommandModule
import discord
from discord.ext import commands
from data import *
from utilities import Table
from utilities.diagnostics import benchmark
from utilities.diagnostics import verboseError
from config import Config
import aiohttp    
import io

class ServerStats(BaseCommandModule):
    """Config Model"""
    def __init__(self, bot):
         self.bot = bot

    @commands.command()
    @verboseError
    @benchmark
    async def online(self, ctx, param = ""):
        result = PlayersOnline_Result.execute()

        #ALL Shows complete table
        if param == "all": 
            table = Table("Server","Online","IP", "Status", "Version", "Resetting")

            for r in result:
                table.addRow(r.FKServerId, 
                                r.TotalPlayersOnline, 
                                str(r.IP or ''),
                                r.Status,
                                str(r.Version or ''),
                                "True" if r.IsResetting else "False")

        #Default View: shows condenced for mobile 
        else: 
            table = Table("Server","Online")

            for r in result:
                table.addRow(r.FKServerId, 
                                r.TotalPlayersOnline)

        await ctx.send(table.toString())

    @commands.command()
    @verboseError
    @benchmark
    async def rockets(self, ctx):
        msg = await ctx.send("getting file")

        async with aiohttp.ClientSession() as session:

            url = Config.cfg.imageUrls.rockets

            async with session.get(url) as resp:
                if resp.status == 200:
                    buffer = io.BytesIO(await resp.read())

        await ctx.send(file = discord.File(buffer,"stat.png")) 
        await msg.delete()

def setup(bot):
    bot.add_cog(ServerStats(bot))
