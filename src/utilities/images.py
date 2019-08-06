import aiohttp
from config import Config
import math


async def getRockets(daysAgo:int):        
    async with aiohttp.ClientSession() as session:

        url = Config.cfg.imageUrls.rockets
        url = url.format(-abs(daysAgo))

        async with session.get(url) as resp:
            if resp.status == 200:
                buffer = io.BytesIO(await resp.read())

        return buffer
                    
                   