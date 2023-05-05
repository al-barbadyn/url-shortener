import asyncio

import pytest as pytest
from httpx import AsyncClient

from app import app


@pytest.fixture(scope="session")
def event_loop():
    return asyncio.get_event_loop()


@pytest.fixture(scope="session")
async def test_client():
    """
    Regular http client for test. You can use it for anonymous user
    """
    base_url = "http://localhost.com"

    async with AsyncClient(app=app, base_url=base_url) as client:
        yield client
