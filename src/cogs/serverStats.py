from baseCommandModule import BaseCommandModule
import discord
from discord.ext import commands
from data import *
from utilities import Table
from utilities.diagnostics import executionTime

class ServerStats(BaseCommandModule):
    """Config Model"""
    def __init__(self, bot):
         self.bot = bot

    def initCommandModule():
        pass

    @commands.command()
    async def ping2(self, ctx):
        await ctx.send("pong from: serverStats")

    @commands.command()
    async def online(self, ctx):
        try:
            result = PlayersOnline_Result.execute(self._session)

            table = Table("Server","Online","IP", "Status", "Version", "Online")

            for r in result:
                table.addRow(r.FKServerId, 
                             r.TotalPlayersOnline, 
                             str(r.IP or ''),
                             r.Status,
                             str(r.Version or ''),
                             r.IsResetting)

            await ctx.send(table.toString())
        except Exception as e:
           await ctx.send(str(e))

def setup(bot):
    bot.add_cog(ServerStats(bot))
