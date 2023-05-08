import validators
from fastapi import Body
from pydantic import BaseModel, validator


class UrlInputModel(BaseModel):
	url: str = Body(..., embed=True)

	@validator("url")
	def valid_url(cls, v):
		if not validators.url(v):
			raise ValueError("Must be an url")
		return v


class ShortUrlInputModel(BaseModel):
	short_url: str = Body(..., embed=True)
