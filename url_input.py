import sys

class UrlInput:
	def __init__(self):
		self.__params = sys.argv
		self._showMetaData = False

	def GetAllUrls(self):
		if self.__params[1] == "--metadata":
			self._showMetaData = True
			return sys.argv[2:]
		else:
			return sys.argv[1:]