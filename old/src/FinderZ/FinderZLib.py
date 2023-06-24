import os
import subprocess
import shutil

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
	#Used for display purposes:
	def expandListInfo(list):
		amountData = len(list)
		iterator = int(0)
		for i in range(amountData):
			placeHolder = str(list[iterator])
			print(placeHolder + "\n")
			iterator += 1
	#Get contents of file:
	def getFileLineContents(filePath):
		f = open(filePath, 'r')
		lines = f.readlines()
		return lines
	#Get tile line amount
	def getFileLineAmount(filePath):
		f = open(filePath, 'r')
		lines = f.readlines()
		amount = len(lines)
		return amount
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
	
	#Scan files recursively for content:
	def scanFilesForContent(filePath, contentKeyWord, fileExtension):
		Check = False
		for folder, dirs, files in os.walk(filePath):
			if Check == True:
				break
			for file in files:
				if file.endswith(fileExtension):
					fullpath = os.path.join(folder, file)
					with open(fullpath, 'r') as f:
						for line in f:
							if contentKeyWord in line:
								Check = True
								return fullpath
								break
						
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
	
	#Recursively find and replace file content(Dangerous if not used correctly!):
	def findAndReplace(filePath, keyWord, replacementKeyword):
		#Scan for files:
		
		for folder, dirs, files in os.walk(filePath):
			Check = False
			if Check == True:
				break
			for file in files:
				
				fullpath = os.path.join(folder, file)
				
				readable = False
				#Open the file and start scanning:
				fileObject = open(fullpath, 'r')
				
				#Read the lines:
				try:
					fileLines = fileObject.readlines()
					readable = True
				except UnicodeDecodeError:
					print("I: Bypassing some un-decodable files...")
					continue
				#Get the line amount:
				if readable == True:
					lineamount = len(fileLines)
					linecount = 0
					for i in range(lineamount):
						#Line location
						
						#Check if the keyword is in the lineCount:
						if keyWord in fileLines[linecount]:
							Check = True
							
							#Get the info in that line.
							foundLocation = fileLines[linecount]
							
							#Replace the word in the line with the new word.
							replacement = foundLocation.replace(keyWord, replacementKeyword)
							
							#Set the line equal to the new value:
							fileLines[linecount] = replacement
						linecount += 1
				#If the check is True, write the file, else, go back to loop and scan for other files.
					if Check == True:
						f = open(fullpath, 'w')
						f.writelines(fileLines)
	#moveFiles from one place, to the next
	def moveFile(originalFileDir, newFileDir):
		shutil.move(originalFileDir, newFileDir)
		return True
	def copyFile(originalFileDir, newFileDir):
		shutil.copy(originalFileDir, newFileDir)
		return True
	
	#For dealing with directories:
	
	#Used to move a directory:
	def moveDir(originalDir, newDir):
		shutil.move(originalDir, newDir)
		return True
	#Copy a directory and its contents from one place to another:
	def copyDir(originalDir, newDir):
		lastdir = os.path.basename(os.path.normpath(originalDir))
		newDirectory = newDir + "/" + lastdir
		shutil.copytree(originalDir, newDirectory)
		return True
	
	#VERSION 1.2.1
	def renameFile(newName, filePath):
		#Remove any slash marks:
		newFilePath = os.path.dirname(filePath)
		os.rename(filePath, newFilePath + "/" + newName)
		
	def renameDirectory(newName, directoryPath):
		newDirectoryPath = os.path.dirname(os.path.dirname(directoryPath))
		os.rename(directoryPath, newDirectoryPath + "/" + newName)

	#Version 1.2.3:
	def insertTextInFile(insertionText, lineNumber, filePath, appendNewLines = False):
			
		if lineNumber < 1:
			raise Exception("ERR: Line number can not be less than 1.")
		#Open the file and start scanning:
		fileObject = open(filePath, 'r')
		
		
		#Read the lines, if it fails, then raise exception:
		try:
			fileLines = fileObject.readlines()
			readable = True
		except UnicodeDecodeError:
			
			raise Exception("ERR: The file seems to be un-decodable.")
		
		#Check if the file has any content in the first place, and if it doesn't, append a value to avoid errors:
		if fileLines == []:
			fileLines.append("")



		#Get the line amount:
		lineamount = len(fileLines)

		#Define the main line iterator, which starts at 1:
		line = 1

		#For each line...
		for i in range(lineamount):
			
			#Check if the line is in the lineCount to see if the destination has been reached:
			if int(line) == int(lineNumber):
				#Set Check = True
				Check = True
				
				
				#Get the info in that line.
				foundLine = fileLines[line-1]
				
				#Add on to the line contents.
				
				insertion = foundLine + insertionText
				#Set the line equal to the insertion:
				fileLines[line-1] = insertion.replace("\n", '', 1) + "\n"
				
				break

			elif int(line) == int(len(fileLines)) and appendNewLines == True:
				
				#Replace any initial "\n" in the initial contents (to avoid ghost indents)
				fileLines[line-1] = fileLines[line-1].replace('\n', '', 1)

				#While the specified lineNumber is not reached yet, append a new line for each remaining line.
				while int(line) != (lineNumber):
					
					fileLines.append('')
					fileLines[line-1] = fileLines[line-1] + "\n"
					
					line += 1
				
				insertion = fileLines[lineNumber-1] + insertionText
				#Set the line equal to the insertion:
				fileLines[lineNumber-1] = insertion.replace("\n", '', 1)
				
				Check = True
			else:
				#Set the check = False
				Check = False
			line += 1
	#If the check is True, then write the lines to the file. Else, raise exception as no line was found.
		if Check == True:
			f = open(filePath, 'w')
			
			f.writelines(fileLines)
		#If the Check == False, then raise this exception:
		else:
			raise Exception("ERR: No specified line number found in file.")
	#VERSION: 1.2.4
    #Create a single file:
	def createFile(fileName, path):
		os.chdir(path)
		f = open(fileName, 'w')
		f.close()
	#Remove a single file:
	def removeFile(filePath):
		os.remove(filePath)
#Class to call bash scripts (Gives even more flexibilty):
class callBash:
	def runFile(path):
		os.system("chmod +x " + path)
		subprocess.run([path], shell = True)
		