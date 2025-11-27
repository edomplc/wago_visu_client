# WAGO PLC VISU Client

Async Python library for WAGO 750-series PLCs with Codesys 2.3 WebVisu.

Usage:

on init provide
- IP of the PLC as string, for example '192.168.1.3'
- session 

.get_data(addrs)

addrs is an array of visu addresses as strings, for example ['2|112|1|0','2|113|1|0']
returns an array of string values like ['1','0']

.set_data(address, value)

address is a string representing address to write to like '3|1436|1|0'
value is a string with avalue to write to PLC liek '234'

Example:
```
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
```