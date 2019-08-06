import traceback
import sys
from discord.ext import commands
import discord
from config import Config
import traceback

class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """The event triggered when an error is raised while invoking a command.
        ctx   : Context
        error : Exception"""

        if hasattr(ctx.command, 'on_error'):
            return
        
        ignored = (commands.CommandNotFound)
        error = getattr(error, 'original', error)
        
        if isinstance(error, ignored):
            return

        elif isinstance(error, commands.DisabledCommand):
            return await ctx.send(f'{ctx.command} has been disabled.')

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                return await ctx.author.send(f'{ctx.command} can not be used in Private Messages.')
            except:
                pass

        elif isinstance(error, commands.BadArgument):
                return await ctx.send(error.args[0])

        elif isinstance(error, commands.MissingRequiredArgument):           
            return  await ctx.send( f"{error} \n*[{error.param}]*")
            
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

        #TODO enable once in production
        #if Config.cfg.debugMode:
        test = self.exception_to_string(error)
        await ctx.send(test)

    def exception_to_string(self, excp):
        stack =  traceback.extract_tb(excp.__traceback__)  # add limit=?? 
        pretty = traceback.format_list(stack)
        group = ''.join(pretty) + '\n {} {}'.format(excp.__class__,excp)
        return  f"```prolog\n{group}```"
                           

def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))
