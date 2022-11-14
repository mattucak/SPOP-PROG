class Game():
	def __init__(self, name:str, headers:list[str], data:list[str]) -> None:
		self.name = name
		self.headers = headers
		self.data = data

	def __repr__(self) -> str:
		return self.name