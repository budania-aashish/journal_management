import csv

def changeReadableFormat(text,s):
   result = ""
   # transverse the plain text
   for i in range(len(text)):
      char = text[i]
      # Encrypt uppercase characters in plain text
      
      if (char.isupper()):
         result += chr((ord(char) + s-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
      else:
         result += chr((ord(char) + s - 97) % 26 + 97)
   return result
#check the above function

def rowSetUp(row):
	for i in range(0,3):
		row[i]=changeReadableFormat(row[i],s)
	return row

row=['j','k','l']
s=10

with open('file',"a") as csvFile:
			row=rowSetUp(row)
			writer=csv.writer(csvFile)
			writer.writerow(row)
csvFile.close()

filename='file'
with open(filename, "r") as csvFile:
				    for row in reversed(list(csv.reader(csvFile))):
				       	time=changeReadableFormat(row[0],10)
				       	txt=changeReadableFormat(row[1],10)
				       	abcs=changeReadableFormat(row[2],10)
				       	print(time+ ' '+txt +' '+abcs)
csvFile.close()