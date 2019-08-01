import discord
from data import *
from baseCommandModule import BaseCommandModule
from discord.ext import commands
from utilities import Table
from utilities.diagnostics import verboseError
import aiohttp    
import io

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
    async def t3(self, ctx):
        msg = await ctx.send("getting file")

        async with aiohttp.ClientSession() as session:
            url = "http://dlpi02.poli.fun:3000/render/d-solo/qS5B5IVWz/factorio-status?orgId=1&refresh=5m&from=1564635600000&to=1564696097219&panelId=10&width=1000&height=500&tz=America%2FChicago"
            async with session.get(url) as resp:
                if resp.status == 200:
                    buffer = io.BytesIO(await resp.read())

        await ctx.send(file = discord.File(buffer,"stat.png")) 
        await msg.delete()

    @commands.command()
    @verboseError
    async def t4(self, ctx, prop: int):
        await ctx.send(f"t4  prop: {prop}")

    @t4.error
    async def t4_error(*args):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(error)
        
def setup(bot):
    bot.add_cog(Debug(bot))
