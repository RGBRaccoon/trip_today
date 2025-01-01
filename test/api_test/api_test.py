import app
import pytest
from httpx import AsyncClient


@pytest.mark.asyncio  # @pytest.mark.anyio를 변경한 예제
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Tomato"}
