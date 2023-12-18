import pytest
from unittest.mock import AsyncMock

from my_aiogram.handlers import done

@pytest.mock.asyncio
async def test_podpiska():
    await done()

