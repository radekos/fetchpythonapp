class FileWriter:
	def writeToFile(self, fileName, content):
		file = open(fileName, "w", -1, "utf-8")
		file.write(content)
		file.close()