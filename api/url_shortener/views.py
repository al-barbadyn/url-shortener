from fastapi import Request, HTTPException

from api.url_shortener.input import UrlInputModel, ShortUrlInputModel
from apps.url_shortener.models import ShortUrl


async def create_short_url(body: UrlInputModel, request: Request):
	short_url = await ShortUrl.add_ulr(url=body.url)
	return {"short_url": request.base_url._url + short_url}


async def delete_short_url(body: ShortUrlInputModel):
	is_deleted = await ShortUrl.delete_short_url(short_url=body.short_url)
	if not is_deleted:
		raise HTTPException(status_code=404, detail="Short url not found")

	return {"status": "Success"}
