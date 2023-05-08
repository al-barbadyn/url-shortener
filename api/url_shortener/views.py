from fastapi import Request, HTTPException

from api.url_shortener.input import UrlInputModel, ShortUrlInputModel
from apps.url_shortener.models import ShortUrl


async def create_short_url(body: UrlInputModel, request: Request):
	short_url = await ShortUrl.add_ulr(url=body.url)
	return {"short_url": request.base_url._url + short_url}


async def delete_short_url(body: ShortUrlInputModel, request: Request):
	not_found_exception = HTTPException(status_code=404, detail="Short url not found")
	short_url = body.short_url.split("/")[-1]
	base_url = body.short_url.replace(short_url, "")
	if request.base_url._url != base_url:
		raise not_found_exception

	short_url = body.short_url.split("/")[-1]
	is_deleted = await ShortUrl.delete_short_url(short_url=short_url)
	if not is_deleted:
		raise not_found_exception

	return {"status": "Success"}
