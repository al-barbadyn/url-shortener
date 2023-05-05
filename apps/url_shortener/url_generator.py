import random
import string

from config import config


class UrlGenerator:
	def __init__(self):
		self._length = config.URL_LENGTH
		self._characters = list(string.ascii_letters + string.digits)

	def generate(self) -> str:
		password = ""
		for _ in range(self._length):
			password += random.choice(self._characters)

		return password


url_generator = UrlGenerator()
