import discord
from data import *
from baseCommandModule import BaseCommandModule
from discord.ext import commands
from utilities import Table

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
                table.addRow(r.fk_server, r.number_of_players_connected)

            await ctx.send(table.toString())
        except Exception as e:
            await ctx.send(str(e))
        
def setup(bot):
    bot.add_cog(Debug(bot))