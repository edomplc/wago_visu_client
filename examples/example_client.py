import asyncio
import aiohttp

from wago_visu_client import WagoPLC, APIConnectionError

session = aiohttp.ClientSession

async def main():
    async with aiohttp.ClientSession() as session:  
        plc = WagoPLC("192.168.10.3", session) 
        try:
            values = await plc.get_data(["2|112|1|0"])
            print("Data:", values)
        except APIConnectionError as e:
            print("Error:", e)
        await asyncio.sleep(1)  # Optional delay

asyncio.run(main())
