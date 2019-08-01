import aiohttp        
import aiofiles

class ImageManager(object):


   async def get_image():        
        async with aiohttp.ClientSession() as session:
            url = "http://dlpi02.poli.fun:3000/render/d-solo/qS5B5IVWz/factorio-status?orgId=1&refresh=5m&from=1564635600000&to=1564696097219&panelId=10&width=1000&height=500&tz=America%2FChicago"
            async with session.get(url) as resp:
                if resp.status == 200:
                    buffer = io.BytesIO(await resp.read())
                    
                   