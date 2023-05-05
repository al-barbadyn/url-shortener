from datetime import datetime

from asyncpg import UniqueViolationError
from sqlalchemy import Column, Integer, String, DateTime, func

from apps.url_shortener import exc
from apps.url_shortener.url_generator import url_generator
from libs.async_pg import adb_session
from libs.pg import Base


class ShortUrl(Base):

	__tablename__ = "short_urls"

	id: int = Column(Integer, primary_key=True)
	url: str = Column(String, unique=True)
	short_url: str = Column(String, unique=True)
	created_at: datetime = Column(DateTime, server_default=func.current_timestamp())

	def __repr__(self):
		return f"URL <{self.url}> short <{self.short_url}>"

	@classmethod
	async def add_ulr(cls, url: str) -> str:
		query = """
			INSERT INTO short_urls (url, short_url)
			VALUES ($1, $2)
			RETURNING short_url
		"""

		async with await adb_session() as conn:
			try:
				result = await conn.fetchrow(query, url, url_generator.generate())
				return result.get("short_url")
			except UniqueViolationError:
				return await cls.get_short_url(url=url)

	@staticmethod
	async def get_url(query: str, url: str):
		async with await adb_session() as conn:
			result = await conn.fetchrow(query, url)

		if not result:
			raise exc.UrlDoesNotExist

		return result.get("url")

	@classmethod
	async def get_short_url(cls, url: str) -> str:
		query = """
			SELECT 
				short_url as url
			FROM short_urls
			WHERE
				url = $1
		"""

		return await cls.get_url(query=query, url=url)

	@classmethod
	async def get_url_by_short_url(cls, short_url: str) -> str:
		query = """
			SELECT 
				url
			FROM short_urls
			WHERE
				short_url = $1
		"""

		return await cls.get_url(query=query, url=short_url)

	@staticmethod
	async def delete_short_url(short_url: str) -> bool:
		query = """
			DELETE FROM short_urls
			WHERE short_url = $1
			RETURNING url
		"""

		async with await adb_session() as conn:
			result = await conn.fetchrow(query, short_url)

		return bool(result)
