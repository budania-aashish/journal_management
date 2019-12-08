import csv
import time
def getRowsCount(filename):
	try:
		with open(filename,"r") as csvFile:
			csvFile = csv.reader(csvFile,delimiter = ",")
			data = list(csvFile)
			row_count = len(data)
		return (row_count)
	except Exception as e:
		return 0

def addJournal(id):
		filename=id+'.csv'
		tm=time.strftime('%d %b %Y %H:%M%p')
		print("Enter text to add")
		txt=input()
		#gets rows count and checks for the threshold for each user 
		if getRowsCount(filename)==4:
			#delet first row 
			rowsOfCsv = []
			csvFile = open(filename)
			reader = csv.reader(csvFile)
			for row in reader:
				if reader.line_num==1:
					continue 
				rowsOfCsv.append(row)
			csvFile.close()
			
			#update csv without first row 
			csvFile = open(filename, "w")
			writer = csv.writer(csvFile)
			for row in rowsOfCsv:
			    writer.writerow(row)
			csvFile.close()

		#Now just add the journal
		row=[]
		row.append(tm)
		row.append(txt)
		with open(filename,"a") as csvFile:
			writer=csv.writer(csvFile)
			writer.writerow(row)
		csvFile.close()
		print("Congrats! You have added a journal file")

def popUpAgain(passwd,flag):
	if flag==0:
		print("Enter password again ")
		pwd=input()
		if pwd==passwd:
			print("Good job! Authentication successful!")
			dealwithApp(id,pwd)
		else:
			print("Come on! You entered wrong password again")
			flag=0
			popUpAgain(passwd,flag)
			
def getUsersCount():
	try:
		with open('users.csv',"r") as csvFile:
			csvFile = csv.reader(csvFile,delimiter = ",")
			data = list(csvFile)
			row_count = len(data)
		#print("users count is ",row_count)
		return (row_count)
	except Exception as e:
		print("Welcome you are the first User")
		return 0

#when user tries to login without creating an account 
def dealwithACase(id,pwd):
			print("User doesn't exist, First create an account")
			print("Enter 1 to register with entered Id and password else enter any key to exit")
			ch=input()
			print()
			if ch=='1':
				signUp(id,pwd,1)
			else:
				print("Exiting")
				print()

def checkIfUserDoesNotExists(id,pwd):
	try:
		with open('users.csv',"r") as csvFile:
				reader = csv.reader(csvFile)
				for row in reader:
					if row[0]==id:
						return True
		return False 
	except Exception as e:
		dealwithACase(id,pwd)
	

def checkIfExists(id,pwd,flag):
	with open('users.csv',"r") as csvFile:
				reader = csv.reader(csvFile)
				for row in reader:
					if row[0]==id:
						print("Come on, think different! This id also exists try with some other id")
						print()
						return True
	signUp(id,pwd,1)

def printFile(id,pwd):
	filename=id+'.csv'
	try:
		with open(filename, "r") as csvFile:
				    for row in reversed(list(csv.reader(csvFile))):
				       	time=row[0]
				       	txt=row[1]
				       	print(time+ ' '+txt)
		csvFile.close()
	except:
		print("Nothing to show! First add some journals")
		dealwithApp(id,pwd)

def dealwithApp(id,pwd):
	filename=id+'.csv'
	print("Select 1. Add new journal 2. List all 3. exit =>")
	ch=input()
	if ch=='3':
		exit()
	elif ch!='1' and ch!='2' and ch!='3':
		print("Invalid choice")
		print()
		dealwithApp(id,pwd)
	elif ch=='1':
		addJournal(id)
		dealwithApp(id,pwd)
	elif ch=='2':
			printFile(id,pwd)
			dealwithApp(id,pwd)

def login(id,pwd):
		try:
			with open('users.csv',"r") as csvFile:
				reader = csv.reader(csvFile)
				for row in reader:
					if row[0]==id:
						if row[1]==pwd:
							print("Authentication is successful! ")
							dealwithApp(id,pwd)
							break
						else:
							print("Invalid password :( ")
							print()
							flag=0
							popUpAgain(row[1],flag)
			csvFile.close()
		except Exception as e:		
			print("User doesn't Exist :(")
			print("First register with id and password")
			print("Enter 1 to register with entered Id and password else enter any key to exit")
			ch=input()
			print()
			if ch=='1':
				signUp(id,pwd,1)
			else:
				print("Exiting")
				print()

def signUp(id,pwd,flag):
	if flag==0:
		print("Enter id")
		id=input()
		print("Enter password")
		pwd=input()
		if(checkIfExists(id,pwd,flag)):
			signUp(id,pwd,flag)
	else:
			row=[]
			row.append(id)
			row.append(pwd)
			with open('users.csv', "a") as csvFile:
				writer = csv.writer(csvFile)
				writer.writerow(row)
			csvFile.close()
			print("Created an account")
			print("Please don't forget your password")
			dealwithApp(id,pwd)

def main():
	print("Welcome to the journal management! ")
	print("Enter 1 for signup and 2 for login and 3 for exit")
	ch=input()
	if ch!='1' and ch!='2':
		print("Invalid choice")
	elif ch=='1':
		if getUsersCount()>3:
			print("Sorry to tell you that max 10 people are allowed to access the services, you came late :(")
			exit()
		print("Enter id")
		id=input()
		print("Enter password")
		pwd=input()
		flag=1
		#need to check whether id exists or not 
		try:
			with open('users.csv',"r") as csvFile:
					reader = csv.reader(csvFile)
					for row in reader:
						if row[0]==id:
							print("This id exists try with some other id")
							flag=0
							signUp(id,pwd,flag)
			#print("This id doesn't exists")
			flag=1
			signUp(id,pwd,flag)
		except Exception as e:
			print("Congratulation on being first user")
			signUp(id,pwd,flag)
	elif ch=='2':
		print("Enter id")
		id=input()
		print("Enter password")
		pwd=input()
		if checkIfUserDoesNotExists(id,pwd):
			login(id,pwd)
		else:
			dealwithACase(id,pwd)

	elif ch=='3':
		exit()
	else:
		print("Invalid choice")
		print()
		exit()

if __name__ == '__main__':
	main()