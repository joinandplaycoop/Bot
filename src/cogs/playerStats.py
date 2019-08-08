import discord
from data import *
from baseCommandModule import BaseCommandModule
from discord.ext import commands
from sqlalchemy import func
import utilities.images as img

class PlayerStats(BaseCommandModule):
    """Cog of PlayerStats"""
    def __init__(self, bot):
        self.bot = bot
        
    #@commands.command()
    #async def ping1(self, ctx):
    #    test = self._session.execute(func.upper('PlayersOnline')).scalar()

    #    query = 'call PlayersOnline'
    #    #result = self._session.execute(query).fetchall()

    #    result2 = PlayersOnline_Result.execute(self._session)

    #    await ctx.send("pong from: playerStats")

    @commands.command()
    async def played(self, ctx, userName:str, daysAgo:int=7):
        """Playtime graph from player X from Y days ago
            played [player][daysAgo]
        """
        msg = await ctx.send("Getting the file :arrows_counterclockwise:")        
        buffer = await img.getPlaytime(userName,daysAgo)
        content = f"`Playtime of {userName} from {daysAgo} days ago until now`"
        await ctx.send(file = discord.File(buffer,"stat.png"), content=content) 
        await msg.delete()

    @commands.command()
    async def joined(self, ctx, member: discord.Member):
        """Says when a member joined."""
        await ctx.send('{0.name} joined in {0.joined_at}'.format(member))


def setup(bot):
    bot.add_cog(PlayerStats(bot))


