from urllib.parse import urlparse
from multiprocessing import Process
from dataclasses import dataclass

from url_input import UrlInput
from url_downloader import UrlDownloader
from file_writer import FileWriter

@dataclass
class HtmlFile:
	lastFetch: str
	siteName: str
	imageCount: int
	linkCount: int

def downloadAndWrite(url, urlDownloader, fileWriter, showMetaData):
	try:
		urlParsed = urlparse(url)
		siteName = "{}{}".format(urlParsed.netloc, urlParsed.path.replace("/", "_"))

		urlDownloadResult = urlDownloader.downloadHTML(url, siteName, fileWriter)
		htmlFile = HtmlFile(urlDownloadResult[0], siteName, urlDownloadResult[1], urlDownloadResult[2])

		if showMetaData:
			print("""
			site: {}
			num_links: {}
			images: {}
			last_fetch: {}
			""".format(htmlFile.siteName, htmlFile.linkCount, htmlFile.imageCount, htmlFile.lastFetch))

	except Exception as error:
		print("Error for {}".format(siteName), error)

def main(urlDownloader, fileWriter, urlInput):
	for url in urlInput.GetAllUrls():
		p = Process(target=downloadAndWrite, args=(url, urlDownloader, fileWriter, urlInput._showMetaData))
		p.start()
		p.join()
		
if __name__ == "__main__":
	main(urlDownloader=UrlDownloader(), fileWriter=FileWriter(), urlInput=UrlInput())