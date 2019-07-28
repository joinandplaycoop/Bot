import discord
from baseCommandModule import BaseCommandModule
from discord.ext import commands

class PlayerStats(BaseCommandModule):
    """Cog of PlayerStats"""
    def __init__(self, bot):
        self.bot = bot

    def initCommandModule():
        print("initCommandModule: PlayerStats")

    @commands.command()
    async def ping1(self, ctx):
        await ctx.send("pong from: playerStats")

    @commands.command()
    async def joined(ctx, member: discord.Member):
        """Says when a member joined."""
        await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

def setup(bot):
    bot.add_cog(PlayerStats(bot))