import asyncio

from asyncpg import Pool, create_pool

from config import config


shared_event_loop = asyncio.get_event_loop()


class PoolConnection:
	def __init__(self, pool: Pool):
		self.pool = pool

	async def __aenter__(self):
		self.conn = await self.pool.acquire()
		return self.conn

	async def __aexit__(self, exc_type, exc_val, exc_tb):
		await self.pool.release(self.conn)


class AsyncPgConnection:
	def __init__(self, pg_uri: str):
		self.pool = None
		self.pg_uri = pg_uri

	async def __call__(self, *args, **kwargs):
		if not self.pool:
			self.pool = await create_pool(
				dsn=self.pg_uri,
				loop=shared_event_loop,
			)

		return PoolConnection(self.pool)


adb_session = AsyncPgConnection(pg_uri=config.DB_URI)
