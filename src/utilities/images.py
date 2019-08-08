import aiohttp
from config import Config
import math
import io

async def getRockets(daysAgo:int = 0):        
    async with aiohttp.ClientSession() as session:

        url = Config.cfg.imageUrls.rockets

        days = str(-abs(daysAgo)) + "d" if daysAgo != 0 else ""
        url = url.format(days)

        async with session.get(url) as resp:
            if resp.status == 200:
                buffer = io.BytesIO(await resp.read())

        return buffer

async def getPlaytime(playerName :str, daysAgo:int = 7):        
    async with aiohttp.ClientSession() as session:

        url = Config.cfg.imageUrls.playTime

        days = str(-abs(daysAgo)) + "d" if daysAgo != 0 else ""

        url = url.format(days,playerName)

        async with session.get(url) as resp:
            if resp.status == 200:
                buffer = io.BytesIO(await resp.read())

        return buffer
                    
                   