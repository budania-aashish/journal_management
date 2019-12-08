import csv
def printFile():
	filename='1.csv'
	with open(filename, "rb") as csvFile:
		for row in reversed(list(csv.reader(csvFile))):
				       	time=row[0]
				       	txt=row[1]
				       	print(time+ ' '+txt)
	csvFile.close()
printFile()