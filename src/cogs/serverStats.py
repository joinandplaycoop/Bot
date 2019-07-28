from baseCommandModule import BaseCommandModule
import discord
from discord.ext import commands

class ServerStats(commands.Cog):
    """Config Model"""
    def __init__(self, bot):
         self.bot = bot

    def initCommandModule():
        pass

    @commands.command()
    async def ping2(self, ctx):
        await ctx.send("pong from: serverStats")


def setup(bot):
    bot.add_cog(ServerStats(bot))