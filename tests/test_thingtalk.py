"""Tests for ThingTalk."""
import pytest

import aiohttp

from opp_net import thingtalk

API_URL = "https://example.com"
CONVERT_URL = f"{API_URL}/convert"


@pytest.fixture(autouse=True)
def set_api_url(cloud_mock):
    """Set TT API url."""
    cloud_mock.thingtalk_url = API_URL


async def test_async_convert_ok(aioclient_mock, cloud_mock):
    """Test async convert."""
    aioclient_mock.post(CONVERT_URL, json={"hello": "yo"})
    assert await thingtalk.async_convert(cloud_mock, "Hello") == {"hello": "yo"}


async def test_async_convert_fail(aioclient_mock, cloud_mock):
    """Test async convert."""
    aioclient_mock.post(CONVERT_URL, status=400, json={"error": "Convert Error!"})
    with pytest.raises(thingtalk.ThingTalkConversionError) as excinfo:
        await thingtalk.async_convert(cloud_mock, "Hello")

    assert str(excinfo.value) == "Convert Error!"


async def test_async_convert_invalid(aioclient_mock, cloud_mock):
    """Test async convert."""
    aioclient_mock.post(CONVERT_URL, status=500, text="")
    with pytest.raises(aiohttp.ClientResponseError) as excinfo:
        await thingtalk.async_convert(cloud_mock, "Hello")

    assert excinfo.value.status == 500
