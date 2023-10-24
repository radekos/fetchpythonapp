import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime

class UrlDownloader:
	def __init__(self):
		self.__userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.3"

	def downloadHTML(self, url, siteName, fileWriter):
		response = requests.get(url, headers={"User-Agent": self.__userAgent})
		htmlObject = bs(response.content, "html.parser")
		
		imageCount = len(htmlObject.select("img"))
		linkCount = len(htmlObject.select("a"))

		fileWriter.writeToFile(siteName + ".html", str(htmlObject))

		fetchTime = datetime.now()
		return (fetchTime, imageCount, linkCount)