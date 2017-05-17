def linearSearch(searchString):
	searchFile = open("searchFile.txt", "r")

	#list containing all matches
	result = []

	for line in searchFile:
		if searchString.lower() in line.lower():
			result.append(line)

	searchFile.close()
	return result
