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
text = "CEASER CIPHER DEMO"
s = 2

print ("Plain Text : " + text)
print ("Decrypt Text : " + text)
print(changeReadableFormat(text,s))