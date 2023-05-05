from fastapi import APIRouter

from api.url_shortener.output import UrlOutputModel
from api.url_shortener.views import create_short_url, delete_short_url

router = APIRouter(prefix="/api/v1/url-shortener", tags=["Short Url"])


router.add_api_route(
	"/",
	endpoint=create_short_url,
	methods=["POST"],
	response_model=UrlOutputModel,
	status_code=201,
)

router.add_api_route(
	"/",
	endpoint=delete_short_url,
	methods=["DELETE"],
	status_code=204,
)
