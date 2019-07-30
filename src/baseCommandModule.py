import discord
from discord.ext.commands.bot import Bot
from discord.ext import commands
from data.session import Session


class BaseCommandModule(commands.Cog):
    """Base class of all command modules.  All command modules inherit from BaseCommandModule and are placed in the cogs Folder"""

    _subclasses = []
    _session = Session()

    def __init__(self, bot):
        self.bot = bot

    def __init_subclass__(cls, *args, **kwargs):
        super().__init_subclass__(*args, **kwargs)
        cls._subclasses.append(cls)  
        


