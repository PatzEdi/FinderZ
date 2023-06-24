#!/usr/bin/env python3

#Functions that will be used frequently:
import os
import shutil

#UPDATE Version 1.3 (Big update: includes documentation, recursive booleans, improvemenets in reliability, bug fixes)


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
	
	def readDir(dir, returnFiles = True, returnDirectories = True):
		dir1files = GatherInfo.getAllFileNamesinDir(dir)
		
		directories = []
		files = []

		for file in dir1files:
			fullpath = os.path.join(dir, file)
			if os.path.isdir(fullpath) == True:
				directories.append(file)
			else:
				files.append(file)

		if returnFiles == False:
			return directories
		elif returnDirectories == False:
			return files
		else:
			return directories, files
class fileOperands:
	#Find a file based on the exact keyword from a specified path (removed due to the exactSearch parametric variable in the findFiles function!)
	# def findFile(fileName, path, recursive = False):
		
	# 	#If the user wants to scan recursively through directories:
	# 	if recursive == True:
	# 		result = []
	# 		for root, dirs, files in os.walk(path):
	# 			files = ''.join(files)
	# 			if fileName in files:
					
	# 				mainFileDir = os.path.join(root)
	# 				allFiles = GatherInfo.getAllFileNamesinDir(mainFileDir)
	# 				amountFilesInDir = GatherInfo.getResultsAmount(allFiles)
	# 				iterator = 0
	# 				for i in range(amountFilesInDir):
	# 					finder = allFiles[iterator]
	# 					stringed = str(''.join(finder))
	# 					if fileName == stringed:
	# 						result.append(os.path.join(root, stringed))
	# 					iterator += 1
	# 		return result
	# 	#If the user only wants to scan a specific directory, defaults to non-recursive:
	# 	else:
	# 		#Get all the files in the list:
	# 		allFiles = GatherInfo.getAllFileNamesinDir(path)
	# 		amountFilesInDir = GatherInfo.getResultsAmount(allFiles)
	# 		for i in range(amountFilesInDir):
	# 			if fileName == str(allFiles[i]):
	# 				foundFilePath = os.path.join(path, allFiles[i])
	# 				return foundFilePath
	#New recursive option to find files containing a global keyword, and new exactSearch function to replace the whole findFile funtion:
	def findFiles(fileName, path, exactSearch = False, recursive = False):
		#Main results list to return at the end:
		results = []
		
		if recursive == True:
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
						#Exact search parameter to decide whether or not the given keyWord is exact or within the file name to search for:
						if exactSearch == True:
							if fileName == stringed:
								results.append(os.path.join(root, stringed))
						else:
							if fileName in stringed:
								results.append(os.path.join(root, stringed))
						
						iterator += 1
			
		#Else, defaults to single directory that is non-recursive:
		else:
			#Get all the files in the given directory:
			allFiles = GatherInfo.getAllFileNamesinDir(path)
			#Get the amount of files in the directory:
			amountFilesInDir = GatherInfo.getResultsAmount(allFiles)
			#iterate and check if any of the elements in the gathered list of files have a matching keyword:
			for i in range(amountFilesInDir):
				#Exact search parameter to decide whether or not the given keyWord is exact or within the file name to search for:
				if exactSearch == True:
					if fileName == str(allFiles[i]):
						foundFilePath = os.path.join(path, allFiles[i])
					#Append the value:
						results.append(foundFilePath)
				else:
					if fileName in str(allFiles[i]):
						foundFilePath = os.path.join(path, allFiles[i])
					#Append the value:
						results.append(foundFilePath)
		return results
	
	#Scan files for content (fileExtension defaults to 'all', but a specific file extension can also be used:
	def scanFilesForContent(path, contentKeyWord, fileExtension = 'all', recursive = False):
		#The resulting files that were found:
		results = []

		if recursive == True:
			for folder, dirs, files in os.walk(path):
				for file in files:
					fullpath = os.path.join(folder, file)
					#If not 'all', include specific file types:
					if fileExtension != 'all':
						if file.endswith(fileExtension):
							try:
								with open(fullpath, 'r') as f:
									for line in f:
										if contentKeyWord in line:
											results.append(fullpath)
							except:
								pass
					#If the fileExtension is 'all', include all fileTypes:
					elif fileExtension == 'all':
						try:
							with open(fullpath, 'r') as f:
								for line in f:
									if contentKeyWord in line:
										#Append the result:
										results.append(fullpath)
						except:
							pass
		else:
			#Get all the files in the given directory:
			allFiles = GatherInfo.getAllFileNamesinDir(path)
			#Get the amount of files in the directory:
			amountFilesInDir = GatherInfo.getResultsAmount(allFiles)
			#iterate and check if any of the elements in the gathered list of files have a matching keyword:
			for i in range(amountFilesInDir):
				file = allFiles[i]
				filePath = os.path.join(path, file)
				#If it is 'all', include all files:
				if fileExtension == 'all':
					#Check whether or not the file is readable:
					try:
						lineContent = GatherInfo.getFileLineContents(filePath)
						lineAmount = len(lineContent)
						for lines in range(lineAmount):
							line = str(lineContent[lines])
							if contentKeyWord in line:
								results.append(filePath)
					except: 
						pass
				
				elif fileExtension != 'all':
					#Check whether or not the file ends with a specific extension:
					if file.endswith(fileExtension): 
						try:
							lineContent = GatherInfo.getFileLineContents(filePath)
							lineAmount = len(lineContent)
							for lines in range(lineAmount):
								line = str(lineContent[lines])
								if contentKeyWord in line:
									results.append(filePath)
						except: 
							pass
				#Return the main list containing all the directories of the files that include the specific keyword:
		return results
	

	def removeFiles(fileName, path, exactSearch = False, recursive = False):
		result = []
		removeCheck = int(0)
		if recursive == True:
			for root, dirs, files in os.walk(path):
				files = ' '.join(files)
				if fileName in files:
					
					mainFileDir = os.path.join(root)
					allFiles = GatherInfo.getAllFileNamesinDir(mainFileDir)
					amountFilesInDir = GatherInfo.getResultsAmount(allFiles)
					
					for i in range(amountFilesInDir):
						found = False
						finder = allFiles[i]
						stringed = str(''.join(finder))
						#Check if exactSearch is toggled:
						if exactSearch == True:
							if fileName == stringed:
								result.append(os.path.join(root, stringed))
								directory = os.path.join(root, stringed)
								found = True
						else:
							if fileName in stringed:
								result.append(os.path.join(root, stringed))
								directory = os.path.join(root, stringed)
								found = True
							
						#Disclaimers and warnings (Optional, just there for user experience):
						if found == True:	
							print("\n File Found at:\n" + directory)
							warning = "\nYou are about to delete this file. Continue? (1/2): "
							
							agreement = int(input(warning))
							
							if agreement == 1:
								os.remove(directory)
								print("\nRemoved 1 File")
								removeCheck = 1
		else:
			#Get all the list of files:
			allFiles = GatherInfo.getAllFileNamesinDir(path)
			amountFilesInDir = GatherInfo.getResultsAmount(allFiles)
			
			for i in range(amountFilesInDir):
				found = False
				finder = allFiles[i]
				stringed = str(''.join(finder))
				
				if exactSearch == True:
					if fileName == stringed:
						result.append(os.path.join(path, stringed))
						directory = os.path.join(path, stringed)
						found = True
				else:
					if fileName in stringed:
						result.append(os.path.join(path, stringed))
						directory = os.path.join(path, stringed)
						found = True
							
				#Disclaimers and warnings (Optional, just there for user experience and security):
				if found == True:	
					print("\n File Found at:\n" + directory)
					warning = "\nYou are about to delete this file. Continue? (1/2): "
					
					agreement = int(input(warning))
					
					if agreement == 1:
						os.remove(directory)
						print("\nRemoved 1 File")
						removeCheck = 1
				
		if removeCheck == 1:
			print(f"\nAll selected files with keyword '{fileName}' successfully removed.")
		elif removeCheck != 1:
			print(f"\nNo files removed or found with the keyword '{fileName}'")
	

	#Recursively find and replace file content(Dangerous if not used correctly!):
	def findAndReplaceInFiles(path, keyWord, replacementKeyword, recursive = True):
		#Scan for files:
		if recursive == True:
			for folder, dirs, files in os.walk(path):
				for file in files:

					Check = False
					readable = False
					fullpath = os.path.join(folder, file)

					#Read the lines:
					try:
						#Open the file and start scanning:
						fileObject = open(fullpath, 'r')
						fileLines = fileObject.readlines()
						readable = True
					except UnicodeDecodeError:
						pass
					#Get the line amount:
					if readable == True:
						
						
						for i in range(len(fileLines)):
							#Line location
							
							#Check if the keyword is in the lineCount:
							if keyWord in fileLines[i]:
								Check = True
								
								#Get the info in that line.
								foundLocation = fileLines[i]
								
								#Replace the word in the line with the new word.
								replacement = foundLocation.replace(keyWord, replacementKeyword)
								
								#Set the line equal to the new value:
								fileLines[i] = replacement
							
						#If the check is True, write the file, else, go back to loop and scan for other files.
						if Check == True:
							f = open(fullpath, 'w')
							f.writelines(fileLines)
		else:
			#Get all the file names in a list:
			files = GatherInfo.readDir(path, returnDirectories = False)

			for file in files:
				Check = False
				readable = False
				filePath = os.path.join(path, file)
				try:
					contents = GatherInfo.getFileLineContents(filePath)
					readable = True
				except UnicodeDecodeError:
					readable = False

				if readable == True:
					#Scan the 
					for i in range(len(contents)):
						if keyWord in contents[i]:
							Check = True
							#replace:
							contents[i] = contents[i].replace(keyWord, replacementKeyword)
					
				if Check == True:
					f = open(filePath, 'w')
					f.writelines(contents)

				
					
	#New insert text in file function! (Works very well now unlike pervious version).
	def insertTextInFile(insertionText, lineNumber, filePath, appendNewLines = False):
		#Check if the lineNumber is valid:
		if lineNumber < 1:
			raise Exception("ERR: Line number can not be less than 1")
		#Main file to open:
		try:
			lineContent = GatherInfo.getFileLineContents(filePath)
		except:
			raise Exception("ERR: The file seems to be un-decodable.")
		
		if lineNumber > len(lineContent) and appendNewLines == False:
			raise Exception("ERR: Greater lineNumber value than actual file line amount (Perhaps consider setting 'appendNewLines' to True)")
		#Init appendation of placeholder:
		if lineNumber != len(lineContent):
			lineContent.append('')
		#Appendation of new lines algo:
		if appendNewLines == True and lineNumber > (len(lineContent)-1):
			#Append new lines:
			for i in range(len(lineContent)):
				if '\n' not in lineContent[i]:
					lineContent[i] = lineContent[i] + "\n"
			 
			#lineContent[-1:][0] = lineContent[-1:][0] + "\n"
			while len(lineContent) != (lineNumber):
				lineContent.append("\n")
			lineContent[lineNumber-1] =  insertionText
		#Normal algo that may include everything:
		else:
			if lineNumber == len(lineContent):
				lineContent[lineNumber-1] = lineContent[lineNumber-1] + insertionText
			elif lineNumber < len(lineContent):
				lineContent[lineNumber-1] = lineContent[lineNumber-1].replace("\n", '') + insertionText + "\n"
		
		#Write to the file:
		f = open(filePath,'w')
		f.writelines(lineContent)
	
	#More reliable functions (reduces chance of directory problems):
	def copyDir(originalDir, newDir):
			lastdir = os.path.basename(os.path.normpath(originalDir))
			newDirectory = os.path.join(newDir, lastdir)
			print(newDirectory)
			shutil.copytree(originalDir, newDirectory)
			return True
	def renameFile(newName, filePath):
		#Remove any slash marks:
		newFilePath = os.path.dirname(filePath)
		os.rename(filePath, os.path.join(newFilePath,newName))
		
	def renameDirectory(newName, directoryPath):
		newDirectoryPath = os.path.dirname(os.path.dirname(directoryPath))
		os.rename(directoryPath, os.path.join(newDirectoryPath, newName))


#Finding files:
# file = fileOperands.findFiles("body", "/Users/edwardferrari/RustedWarfareMods/RustedWarfareMods/", exactSearch = False, recursive = True)

# print(file)


#Scanning files for content:
# file = fileOperands.scanFilesForContent("/Users/edwardferrari/MyPythonProjects/GitHubRepos/Active/Finderz/tests", "Hello", recursive = False)

# print(file)
#Insertion text:
#fileOperands.insertTextInFile("10", 1, "/Users/edwardferrari/MyPythonProjects/GitHubRepos/Active/Finderz/tests/insertion.txt", appendNewLines = True)

#fileOperands.copyDir("/Users/edwardferrari/RustedWarfareMods/", "/Users/edwardferrari/RustedWarfareMods/")

# import FinderZ
# FinderZ.fileOperands.createFiles(10, "body", ".txt", "/Users/edwardferrari/RustedWarfareMods/RustedWarfareMods/")

#Remove files:
#fileOperands.removeFiles("body10.txt", "/Users/edwardferrari/RustedWarfareMods/RustedWarfareMods", exactSearch = True, recursive = True)

#Find and replace:
#fileOperands.findAndReplaceInFiles("/Users/edwardferrari/Synchronize/dir3", "Hell", "Heaven", recursive = False)