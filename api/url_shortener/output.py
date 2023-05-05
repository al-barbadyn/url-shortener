from pydantic import BaseModel


class UrlOutputModel(BaseModel):
	short_url: str
