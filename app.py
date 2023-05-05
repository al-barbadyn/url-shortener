from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

from api.url_shortener.routes import router as url_router
from apps.url_shortener import exc
from apps.url_shortener.models import ShortUrl

from config import config

app = FastAPI(debug=config.DEBUG)


app.include_router(url_router)


@app.get("/{short_url:path}")
async def redirect_to_url(short_url: str):
	try:
		url = await ShortUrl.get_url_by_short_url(short_url=short_url)
		return RedirectResponse(url=url)
	except exc.UrlDoesNotExist:
		raise HTTPException(status_code=404, detail="Url not found")

