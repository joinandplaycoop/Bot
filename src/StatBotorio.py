
# Work with Python 3.6
import discord
#from cogs import *
import random
import fnmatch 
import sys
import pkgutil
import importlib
import traceback
import math
from os import listdir
from os.path import isfile, join
from discord.ext import commands
from discord.ext.commands.bot import Bot
from config import Config

description = '''A bot that shows factorio server statistics for joinandplaycoop.'''

client : Bot = commands.Bot(command_prefix = '?', description = description)
client.activity = discord.Game(name='Factorio')
#BaseCommandModule.initCommands(client)

#Events
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello! ' + message.author.display_name)

    await client.process_commands(message)

#commands for dynamic loading/unloading/viewing of cogs.  All cogs are
#automatically loaded from the folder defined in the config
@client.command()
async def load(ctx, extension_name: str):
    """Loads an extension."""
    try:
        cogs_dir = Config.cfg.cogs_dir
        client.load_extension(cogs_dir + "." + extension_name)
    except (AttributeError, ImportError) as e:
        await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await ctx.send("{} loaded.".format(extension_name))

@client.command()
async def unload(ctx, extension_name: str):
    """Unloads an extension."""
    cogs_dir = Config.cfg.cogs_dir
    client.unload_extension(cogs_dir + "." + extension_name)
    await ctx.send("{} unloaded.".format(extension_name))

@client.command()
async def reload(ctx, extension_name: str):
    """Reloads an extension."""
    cogs_dir = Config.cfg.cogs_dir
    client.reload_extension(cogs_dir + "." + extension_name)
    await ctx.send("{} unloaded.".format(extension_name))

@client.command()
async def latency(ctx):
    """Gets the latency of bot to discord."""
    lat = math.floor(client.latency * 1000)
    await ctx.send("`Latency: {}ms`".format(lat))

@client.command()
async def activity(activity: str):
    """Gets the latency of bot to discord."""    
    await client.change_presence(activity=discord.Game(name='Factorio'))

@client.command()
async def cogs(ctx):
    """Gets all .py files in the ./cogs directory"""
    mypath = Config.cfg.cogs_dir
    dir_list = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f.lower().endswith(".py") and not f.startswith("_")]
    
    print(dir_list)
    await ctx.send(dir_list)
    
if __name__ == "__main__":
    cogs_dir = Config.cfg.cogs_dir
    for extension in [f.replace('.py', '') for f in listdir(cogs_dir) if isfile(join(cogs_dir, f)) and f.endswith(".py") and not f.startswith("_")]:
        try:
            client.load_extension(cogs_dir + "." + extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.')
            traceback.print_exc()
    
    client.run(Config.cfg.botToken)
