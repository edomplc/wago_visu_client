# tests/test_api.py
import pytest
import aiohttp
from wago_visu_client import WagoPLC, ConnectionError

@pytest.mark.asyncio
async def test_get_data_success():
    plc_ip = "192.168.10.3"
    addresses = ["2|112|1|0","2|113|1|0"]

    async with aiohttp.ClientSession() as session:  
        plc = WagoPLC(plc_ip, session) 
        values = await plc.get_data(addresses)
        assert values == ["0", "0"]

@pytest.mark.asyncio
async def test_get_data_connection_error():
    plc_ip = "192.168.99.99"
    addresses = ["2|112|1|0","2|113|1|0"]

    async with aiohttp.ClientSession() as session:  
        plc = WagoPLC(plc_ip, session) 

        with pytest.raises(ConnectionError) as exc_info:
            await plc.get_data(addresses)

        assert "timeout" in str(exc_info.value)

