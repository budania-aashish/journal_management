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
row=['4','5','6']
s=2
with open('file',"a") as csvFile:
			for i in range(0,3):
				row[i]=changeReadableFormat(row[i],s)
			writer=csv.writer(csvFile)
			writer.writerow(row)
csvFile.close()