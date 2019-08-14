from discord.ext import commands
from config import Config
import discord
import random

colors = {
  'DEFAULT': 0x000000,
  'WHITE': 0xFFFFFF,
  'AQUA': 0x1ABC9C,
  'GREEN': 0x2ECC71,
  'BLUE': 0x3498DB,
  'PURPLE': 0x9B59B6,
  'LUMINOUS_VIVID_PINK': 0xE91E63,
  'GOLD': 0xF1C40F,
  'ORANGE': 0xE67E22,
  'RED': 0xE74C3C,
  'GREY': 0x95A5A6,
  'NAVY': 0x34495E,
  'DARK_AQUA': 0x11806A,
  'DARK_GREEN': 0x1F8B4C,
  'DARK_BLUE': 0x206694,
  'DARK_PURPLE': 0x71368A,
  'DARK_VIVID_PINK': 0xAD1457,
  'DARK_GOLD': 0xC27C0E,
  'DARK_ORANGE': 0xA84300,
  'DARK_RED': 0x992D22,
  'DARK_GREY': 0x979C9F,
  'DARKER_GREY': 0x7F8C8D,
  'LIGHT_GREY': 0xBCC0C0,
  'DARK_NAVY': 0x2C3E50,
  'BLURPLE': 0x7289DA,
  'GREYPLE': 0x99AAB5,
  'DARK_BUT_NOT_BLACK': 0x2C2F33,
  'NOT_QUITE_BLACK': 0x23272A
}

class Help(commands.Cog):
    """The help menu commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        hidden = True
    )
    async def t8(self, ctx):
        """Tests a crapy embed"""
        embed = Embed()
        embed.setTitleDesc("test title","this is a test description")
        await embed.setThumbnailUrl(ctx,self.bot)

    @commands.command(
       name = "help",
       brief ='The help command!',
       aliases=['commands', 'command', 'h'],
       usage='cog'
    )
    async def help_command(self, ctx, subHelp : str ='all'):
   
       # The third parameter comes into play when
       # only one word argument has to be passed by the user

       # Prepare the embed       
       prefix = Config.cfg.cmdPrefix
       color_list = [c for c in colors.values()]
       help_embed = None
       
       # Get a list of all cogs
       cogs = [c for c in self.bot.cogs.keys()]

       # If cog is not specified by the user, we list all cogs and commands
       if subHelp == 'all':

           help_embed = discord.Embed(
                title='Help Menu',
                description = f"For a list of commands and see source code follow this [link](https://github.com/joinandplaycoop/Bot)\n Also try help with sub commands.  For example:  ```{prefix}help playerStats```__\n\u200B",
                color=random.choice(color_list),
           )

           for subHelp in cogs:

               cog_class = self.bot.get_cog(subHelp)

               # hide hidden cogs from help
               if(getattr(cog_class, 'hidden', False) == True):
                   continue
               
               # Get a list of all commands under each cog
               cog_commands = cog_class.get_commands()

               if len(cog_commands) == 0:
                   continue

               commands_list = ''
               for comm in cog_commands:
                   #hide hidden commands from help
                   if(getattr(comm, 'hidden', False) == True):
                       continue

                   #params
                   params = ""
                   for key, value in comm.clean_params.items():
                         if key == 'param':
                             continue
                         params += f" `[{key}:{value.annotation.__name__}]`"
                   
                   commands_list += f" \u200B \u200B `{prefix}{comm.name}`{params}\n"

                   # Also added a blank field '\u200b' is a whitespace character.
                   if comm == cog_commands[-1]:
                        commands_list += "\u200B"

               # Add the cog's details to the embed.
               help_embed.add_field(
                   name=f"𝄄 __{subHelp}__ 𝄄",
                   value=commands_list,
                   inline=False
               )

       else:
           #specific cog was specified
           lower_cogs = [c.lower() for c in cogs ] 

           # If cog doesn't exist
           if subHelp.lower() not in lower_cogs:
               await ctx.send(f"Invalid cog specified.\nUse `{prefix}help` command to list all cogs.")
               return

           cog = self.bot.get_cog(cogs[ lower_cogs.index(subHelp.lower()) ])
               
            #If cog was hidden
           if getattr(cog, 'hidden', False) == True:
                await ctx.send(f"Cog is hidden. Use `{prefix}help` command to list all valid cogs.")
                return

           help_embed = discord.Embed(
                title=f'Help Menu : ({cog.qualified_name})',
                description = f"__{cog.description}__\n\u200B",
                color=random.choice(color_list),
           ) 

           # Get a list of all commands in the specified cog
           commands_list = cog.get_commands()

           for command in commands_list:
                if(getattr(command, 'hidden', False) == True):
                    continue

                help_text=''

                desc = command.description or command.brief 
                if desc:
                    help_text += f' \u200B \u200B *{desc}*\n'

                #command Aliases
                aliases = ""
                for a in command.aliases:
                    aliases += f"{prefix}{a} "
                help_text += f"**Aliases: \n**`{prefix}{command.name} {aliases}`\n"

                #params
                params = ""
                for key, value in command.clean_params.items():
                        if key == 'param':
                            continue
                        params += f" `[{key}:{value.annotation.__name__}]`"                   
                help_text += f"**Usage: \n** \u200B \u200B `{prefix}{command.name}`{params}\n"
                   
                
                  
                help_text += "\n\u200B"

                help_embed.add_field(
                    name=f"__**{prefix}{command.name}**__",
                    value=help_text,
                    inline=False
                   
                    )                            

       help_embed.set_footer(
           text=f'Requested by {ctx.message.author.name}',
           icon_url=self.bot.user.avatar_url
       )

       await ctx.send(embed=help_embed)
   
       return

def setup(bot):
    bot.add_cog(Help(bot))