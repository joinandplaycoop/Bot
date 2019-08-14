from baseCommandModule import BaseCommandModule
import discord
import utilities.images as img
from discord.ext import commands
from data import *
from utilities import Table
from utilities.diagnostics import benchmark
from utilities.diagnostics import verboseError
from config import Config
import aiohttp    
import io

class ServerStats(BaseCommandModule):
    """These commands are specific for returning stats about the server"""
    def __init__(self, bot):
         self.bot = bot

    @commands.command()
    @verboseError
    @benchmark
    async def online(self, ctx, param=""):
        result = PlayersOnline_Result.execute()

        total = sum(r.TotalPlayersOnline for r in result)

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

        await ctx.send(f" `Total Players Online: {total}` " + table.toString())

    @commands.command()
    @verboseError
    @benchmark
    async def rockets(self, ctx, daysAgo:int=0):
        """Displays graph of total rockets from X days ago
            rockets [daysAgo]
        """
        msg = await ctx.send("Getting the file :arrows_counterclockwise:")
        
        buffer = await img.getRockets(daysAgo)
        content = f"`Rockets from {daysAgo} days ago until now`" if daysAgo != 0 else "`Lastest Rockets`"
        await ctx.send(file = discord.File(buffer,"stat.png"), content=content) 
        await msg.delete()

def setup(bot):
    bot.add_cog(ServerStats(bot))
