import os
import subprocess


#A full library to gather info on files and execute file commands in Python.


#Gather file/general info:
class GatherInfo:
	#mainDirectory to start the findings, gatherings, and main operations.
	def askmainDir():
		mainDirectory = str(input("MainDirectory to iterate over Files: "))
		return mainDirectory
		
	#For finding files with that keyword and displaying how many there are:
	def getResultsAmount(appendedList):
		valueAmount = int(len(appendedList))
		return valueAmount
		
	#Find the amount of files in a directory:
	def getAmountofFilesinDir(mainDir):
		count = 0
		for path in os.listdir(mainDir):
			if os.path.isfile(os.path.join(mainDir, path)):
				count += 1
		return count
	#List all file names in a directory:
	def getAllFileNamesinDir(mainDir):
		dir_list = os.listdir(mainDir)
		return dir_list
	
	def expandListInfo(list):
		amountData = len(list)
		iterator = int(0)
		for i in range(amountData):
			placeHolder = str(list[iterator])
			print(placeHolder + "\n")
			iterator += 1
		
#MainFile operations:	
class fileOperands:
	#Find a single file with a SPECIFIC name (no keyword)
	def findFile(fileName, path):
		result = []
		for root, dirs, files in os.walk(path):
			files = ''.join(files)
			if fileName in files:
				
				mainFileDir = os.path.join(root)
				allFiles = GatherInfo.getAllFileNamesinDir(mainFileDir)
				amountFilesInDir = GatherInfo.getResultsAmount(allFiles)
				iterator = 0
				for i in range(amountFilesInDir):
					finder = allFiles[iterator]
					stringed = str(''.join(finder))
					if fileName == stringed:
						result.append(os.path.join(root, stringed))
					iterator += 1
		return result
	def findFiles(fileName, path):
		result = []
		for root, dirs, files in os.walk(path):
			files = ' '.join(files)
			if fileName in files:

				mainFileDir = os.path.join(root)
				allFiles = GatherInfo.getAllFileNamesinDir(mainFileDir)
				amountFilesInDir = GatherInfo.getResultsAmount(allFiles)
				iterator = 0
				for i in range(amountFilesInDir):
					finder = allFiles[iterator]
					stringed = str(''.join(finder))
					if fileName in stringed:
						result.append(os.path.join(root, stringed))
					iterator += 1
		return result
		
	#Function to remove file with a certain keyword.
	def removeFiles(fileName, path):
		result = []
		removeCheck = int(0)
		for root, dirs, files in os.walk(path):
			files = ' '.join(files)
			if fileName in files:

				mainFileDir = os.path.join(root)
				allFiles = GatherInfo.getAllFileNamesinDir(mainFileDir)
				amountFilesInDir = GatherInfo.getResultsAmount(allFiles)
				iterator = 0
				for i in range(amountFilesInDir):
					finder = allFiles[iterator]
					stringed = str(''.join(finder))
					if fileName in stringed:
						result.append(os.path.join(root, stringed))
						directory = os.path.join(root, stringed)
						
			#Disclaimers and warnings (Optional, just there for user experience):
						
						print("\n File Found at:\n" + directory)
						warning = "\nYou are about to delete this file. Continue? (1/2): "
						
						agreement = int(input(warning))
						
						if agreement == 1:
							os.remove(directory)
							print("\nRemoved 1 File")
							removeCheck == 1
					iterator += 1
				if removeCheck == 1:
					print(f"All selected files with keyword '{fileName}' succesfully removed.")
				elif removeCheck != 1:
					print(f"No files removed or found with the keyword '{fileName}'")
	
	#Create files with a keyword for testing purposes:
	def createFiles(createAmount, keyWord, extensionType, path):
		originalDir = os.getcwd()
		os.chdir(path)
		numExtension = 1
		for i in range(createAmount):
			numExtension = str(numExtension)
			f = open(keyWord + numExtension + extensionType, 'w')
			f.close()
			numExtension = int(numExtension)
			numExtension += 1
		# Return into original directory once complete:
		os.chdir(originalDir)

#Class to call bash scripts (Gives even more flexibilty):
class callBash:
	def runFile(path):
		os.system("chmod +x " + path)
		subprocess.run([path], shell = True)
		