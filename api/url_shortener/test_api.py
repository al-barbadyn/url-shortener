import pytest


@pytest.mark.asyncio
async def test_create_and_delete(test_client):
    response = await test_client.post("/api/v1/url-shortener/", json={"url": "https://translate.google.com"})
    assert response.status_code == 201

    short_url = response.json()["short_url"]
    response = await test_client.post("/api/v1/url-shortener/", json={"url": "https://translate.google.com"})
    assert response.status_code == 201
    assert response.json()["short_url"] == short_url

    response = await test_client.get(short_url)
    assert response.status_code == 307

    response = await test_client.request(
        method="DELETE",
        url="/api/v1/url-shortener/",
        json={
            "short_url": short_url,
        }
    )
    assert response.status_code == 204

    response = await test_client.request(
        method="DELETE",
        url="/api/v1/url-shortener/",
        json={
            "short_url": short_url,
        }
    )
    assert response.status_code == 404

    response = await test_client.get(short_url)
    assert response.status_code == 404
