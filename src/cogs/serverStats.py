from baseCommandModule import BaseCommandModule
import discord
from discord.ext import commands
from data import *
from utilities import Table

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

            #for row in result:
            table = Table("Server","Online")

            for r in result:
                table.addRow(r.fk_server, r.number_of_players_connected)

            await ctx.send(table.toString())
        except Exception as e:
            await ctx.send(str(e))


def setup(bot):
    bot.add_cog(ServerStats(bot))