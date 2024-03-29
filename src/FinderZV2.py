#!/usr/bin/env python3

import os
import shutil
import time
import subprocess
import hashlib
import re
import random

class GatherInfo:
	#For finding files with that keyword and displaying how many there are:
	def getResultsAmount(appendedList):
		valueAmount = int(len(appendedList))
		return valueAmount
		
	#Find the amount of files in a directory:
	def getAmountofComponentsinDir(dir, returnAmountFiles = True, returnAmountDirectories = True):
		directories, files = GatherInfo.readDir(dir)
		
		#Get each amount:
		amount_dirs = len(directories)
		amount_files = len(files)
		if returnAmountFiles == False:
			return amount_dirs
		elif returnAmountDirectories == False:
			return amount_files
		else:
			return amount_dirs, amount_files
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
	def getFileLineContents(filePath, returnStringType = False):
		try:
			f = open(filePath, 'r')
		except:
			raise Exception("ERR: The file could not be opened/decoded.")
		if returnStringType == False:
			lines = f.readlines()
		else:
			lines = f.read()
		return lines
	
	#Get tile line amount
	def getFileLineAmount(filePath):
		f = open(filePath, 'r')
		lines = f.readlines()
		amount = len(lines)
		return amount
	
    #New in V2:
    #New function in V2:
	def isEmptyDir(dir):
		directories, files = GatherInfo.readDir(dir)
		if len(directories) == 0 and len(files) == 0:
			return True
		else:
			return False
	#New in V2:
	def computeHash(path):
		h = hashlib.sha1()
		#Add try except block (to avoid duplicate directory errors in Synchronize class
		try:
			file = open(path, 'rb')

			file_size = os.path.getsize(path)
			# If the file is not empty, compute the hash:
			if file_size > 0:
				chunk = 0
				while chunk != b'':
						chunk = file.read(1024)
						h.update(chunk)	
				return h.hexdigest()
			else:
				#Return false if the file is empty. In other words, skip the file:
				return False
		except:
			#Return False if unhashable
			return False
    
    #New in V2: Comparing two lists for at least one common element:
	def isOneInCommon(list1, list2):
		result = False
	
		for x in list1:
	
			for y in list2:

				#Compare the two results:
				if x == y:
					result = True
					return result
		#Return false if not matching:
		return result

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

	def isRegexAndStringMatching(pattern, string, exactMatch = False):
		matched = False
		#Regex goes in here:
		regexp = re.compile(r'%s' % pattern)
		#Check if exactMatch is set to True:
		if exactMatch == True:
			#If exactMatch is True, check if the string exactly matches the pattern.
			if regexp.fullmatch(string):
				matched = True
		else:
			#If exactMatch is not set to True, search if the string contains the pattern.
			if regexp.search(string):
				matched = True
		return matched

	#Get total amount of lines recusrively in a directory, and optionally even files.
	def getTotalInfo(path, returnFileAmount = False, extensionFilters = [], recursive = False):
		totalamount = 0
		fileAmount = 0

		if recursive == True:
			for folder, dirs, files in os.walk(path):
				for file in files:
					
					#If there are extension filters, execute:
					matchesExtension = False
					#For each extension:
					for extension in extensionFilters:
						if file.endswith(extension):
							matchesExtension = True
							break
					#Either there are no file extensions, or, if there are, check if the file ends with the extension:
					if (len(extensionFilters) == 0) or matchesExtension == True:
						fileAmount += 1
						filepath = os.path.join(folder, file)
						try:
							totalamount += GatherInfo.getFileLineAmount(filepath)
						except UnicodeDecodeError:
							pass
		else:
			files = GatherInfo.readDir(path, returnDirectories = False)

			for file in files:
				#If there are extension filters, execute:
					matchesExtension = False
					#For each extension:
					for extension in extensionFilters:
						if file.endswith(extension):
							matchesExtension = True
					
					#Either there are no file extensions, or, if there are, check if the file ends with the extension:
					if (len(extensionFilters) == 0) or matchesExtension == True:
						fileAmount += 1
						filepath = os.path.join(path, file)
						try:
							totalamount += GatherInfo.getFileLineAmount(filepath)
						except UnicodeDecodeError:
							pass

		if returnFileAmount == True:
			return totalamount, fileAmount
		else:
			return totalamount
		
	#New in 2.0.4
	def compareFiles(file1, file2, comparison_output_file = ''):
		with open(file1, 'r') as f1, open(file2, 'r') as f2:
			f1_lines = f1.readlines()
			f2_lines = f2.readlines()
			output_lines = []
			for i, (line1, line2) in enumerate(zip(f1_lines, f2_lines)):
				if line1 != line2:
					difference = f"\nLine {i+1}:\nFile1: {line1} File2: {line2}\n"
					print(difference)
					output_lines.append(difference)
		if comparison_output_file != '':
			f = open(comparison_output_file)
			f.writelines(output_lines)
			f.close()
		return output_lines
	

	# New functions (GatherInfo):
	def wordCount(string): return len(string.split())
		
	def charCount(string): return len(string)
		
	def byteCount(filePath): return os.path.getsize(filePath)

	def getFileStats(filePath):
		try:
			f = open(filePath)
			stringed_contents = f.read()
		except:
			raise Exception("ERR: The file could not be opened/decoded.")
		
		stats = {'Word Count': 0, 'Char Count': 0, 'Byte Count': 0, 'Line Count': 0}
		
		#word count:
		stats["Word Count"] = (GatherInfo.wordCount(stringed_contents))
		
		#char count:
		stats["Char Count"] = (GatherInfo.charCount(stringed_contents))
		
		#byte count:
		stats["Byte Count"] = (GatherInfo.byteCount(filePath))
		
		#line count:
		stats["Line Count"]= (GatherInfo.getFileLineAmount(filePath))
		
		return stats
	
	# New in V2.1.2: (These functions below are all new in V 2.1.2)
	def isHiddenFile(file_path):
		file_name = os.path.basename(file_path)
		if file_name.startswith('.'):
			return True
		else:
			return False
		
	def getAllHiddenFilesInDir(dir):
		hiddenFiles = []
		files = GatherInfo.readDir(dir, returnDirectories = False)
		for file in files:
			filePath = os.path.join(dir, file)
			if GatherInfo.isHiddenFile(filePath):
				hiddenFiles.append(filePath)
		return hiddenFiles
	# Function that returns the amount of each file extension within a directory (either recursively or not):
	def getAmountOfEachFileTypeInDir(dir, recursive = False):
		counter = 0
		# The two main lists that will be concatenated and put into a dictionary:
		extensions = []
		amounts = []
		for root, dirs, files in os.walk(dir):
			if recursive == False and counter != 0:
				break
			# First, get the total amount of extensions:
			for file in files:
				extension = os.path.splitext(file)[1]
				if extension not in extensions:
					# Append the extension to the list:
					extensions.append(extension)
			counter += 1
		# Second, get the amount of each extension once the extensions list is complete:
		for i in range(len(extensions)):
			extension_amount_counter = 0
			counter = 0
			for root, dirs, files in os.walk(dir):
				if recursive == False and counter != 0:
					break
				# First, get the total amount of extensions:
				for file in files:
					extension = os.path.splitext(file)[1]
					if extension == extensions[i]:
						extension_amount_counter += 1

				counter += 1
			# Append the amount to the amounts list:
			amounts.append(extension_amount_counter)
		# Here, create the dictionary:
		extensions = [x for _, x in sorted(zip(amounts, extensions), reverse = True)]
		amounts = sorted(amounts, reverse = True)
		# Create the dictionary:
		extensions_dict = {}
		for i in range(len(extensions)):
			extensions_dict[extensions[i]] = amounts[i]
		return extensions_dict
		
class fileOperands:
	#New recursive option to find files containing a global keyword, and new exactSearch function to replace the whole findFile funtion:
	def findFiles(fileName, path, exactSearch = False, recursive = False, regex = False):
		#Main results list to return at the end:
		results = []
		
		if recursive == True:
			for root, dirs, files in os.walk(path):
				files = ' '.join(files)
				if (fileName in files) or (regex == True):

					mainFileDir = os.path.join(root)
					allFiles = GatherInfo.getAllFileNamesinDir(mainFileDir)
					amountFilesInDir = GatherInfo.getResultsAmount(allFiles)
					iterator = 0
					for i in range(amountFilesInDir):
						finder = allFiles[iterator]
						stringed = str(''.join(finder))

						#Exact search parameter to decide whether or not the given keyWord is exact or within the file name to search for:

						#Check if the user wants to use regex or not:
						if regex == True:
							if GatherInfo.isRegexAndStringMatching(fileName, stringed, exactMatch = exactSearch):
								
								results.append(os.path.join(root, stringed))
						else:
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
			allFiles = GatherInfo.readDir(path, returnDirectories = False)
			#Get the amount of files in the directory:
			amountFilesInDir = GatherInfo.getResultsAmount(allFiles)
			#iterate and check if any of the elements in the gathered list of files have a matching keyword:
			for i in range(amountFilesInDir):
				#Exact search parameter to decide whether or not the given keyWord is exact or within the file name to search for:

				#Check if user wants to use regex or not:
				if regex == True:
					if GatherInfo.isRegexAndStringMatching(fileName, allFiles[i], exactMatch = exactSearch):
						foundFilePath = os.path.join(path, allFiles[i])
						results.append(foundFilePath)
				
				else:
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
	
	#Scan files for content (fileExtension defaults to 'all', but a specific file extension can also be used):
	def scanFilesForContent(contentKeyWord, path, extensionFilters = [], recursive = False, regex = False):
		#The resulting files that were found:
		results = []

		if recursive == True:
			for folder, dirs, files in os.walk(path):
				for file in files:
					fullpath = os.path.join(folder, file)
					
					#Check the extensionFilters list:
					matchingExtension = False
					for extension in extensionFilters:
						if file.endswith(extension):
							matchingExtension = True
							break

					if (len(extensionFilters) == 0) or (matchingExtension == True):
						try:
							with open(fullpath, 'r') as f:
								for line in f:
									#Check if the user wants to use regex or not:
									if regex == True:
										if GatherInfo.isRegexAndStringMatching(contentKeyWord, line):
											results.append(fullpath)
									else:
										if contentKeyWord in line:
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
				
				#Check the extensionFilters list:
				matchingExtension = False
				for extension in extensionFilters:
					if file.endswith(extension):
						matchingExtension = True
						break
				
				if (len(extensionFilters) == 0) or matchingExtension == True:
					#Check whether or not the file is readable:
					try:
						lineContent = GatherInfo.getFileLineContents(filePath)
						lineAmount = len(lineContent)
						for lines in range(lineAmount):
							line = str(lineContent[lines])

							#Check if the user wants to use regex or not:
							if regex == True:
								if GatherInfo.isRegexAndStringMatching(contentKeyWord, line):
									results.append(filePath)
							else:
								if contentKeyWord in line:
									results.append(filePath)
					except: 
						pass
				#Return the main list containing all the directories of the files that include the specific keyword:
		return results
	
	#Removing files:
	def removeFiles(fileName, path, exactSearch = False, extensionFilters = [], recursive = False, regex = False):
		result = []
		removeCheck = int(0)
		if recursive == True:
			for root, dirs, files in os.walk(path):
				files = ' '.join(files)
				if (fileName in files) or (regex == True):
					
					mainFileDir = os.path.join(root)
					allFiles = GatherInfo.getAllFileNamesinDir(mainFileDir)
					amountFilesInDir = GatherInfo.getResultsAmount(allFiles)
					
					for i in range(amountFilesInDir):
						found = False
						finder = allFiles[i]
						stringed = str(''.join(finder))
						
						#extensionFilters:
						matchingExtension = False
						for extension in extensionFilters:
							if stringed.endswith(extension):
								matchingExtension =True
								break
						
						if (len(extensionFilters) == 0) or matchingExtension == True:
							#Check if the user wants to use regex or not:
							if regex == True:
								if GatherInfo.isRegexAndStringMatching(fileName, stringed, exactMatch = exactSearch):
									directory = os.path.join(root, stringed)
									result.append(directory)
									found = True
							else:
								if exactSearch == True:
									if fileName == stringed:
										directory = os.path.join(root, stringed)
										result.append(directory)
										found = True
								else:
									if fileName in stringed:
										directory = os.path.join(root, stringed)
										result.append(directory)
										found = True
								
							#Disclaimers and warnings (Optional, just there for user experience):
							if found == True:	
								print("\n File Found at:\n" + directory)
								warning = "\nYou are about to delete this file. Continue? ((1) Yes / (2) No): "
								
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

				#extensionFilters:
				matchingExtension = False
				for extension in extensionFilters:
					if stringed.endswith(extension):
						matchingExtension = True
						break

				if (len(extensionFilters) == 0) or matchingExtension == True:
					if regex == True:
						if GatherInfo.isRegexAndStringMatching(fileName, stringed, exactMatch = exactSearch):
							directory = os.path.join(path, stringed)
							result.append(directory)
							found = True
					else:
						if exactSearch == True:
							if fileName == stringed:
								directory = os.path.join(path, stringed)
								result.append(directory)
								found = True
						else:
							if fileName in stringed:
								directory = os.path.join(path, stringed)
								result.append(directory)
								found = True
								
					#Disclaimers and warnings (Optional, just there for user experience and security):
					if found == True:	
						print("\n File Found at:\n" + directory)
						warning = "\nYou are about to delete this file. Continue? ((1) Yes / (2) No): "
						
						agreement = int(input(warning))
						
						if agreement == 1:
							os.remove(directory)
							print("\nRemoved 1 File")
							removeCheck = 1
				
		if removeCheck == 1:
			print(f"\nAll selected files with keyword '{fileName}' successfully removed.")
		elif removeCheck != 1:
			print(f"\nNo files removed or found with the keyword '{fileName}'")
	
    #Create files with a keyword for testing purposes:
	def createFiles(createAmount, keyWord, extensionType, path, firstFileStartsAtOne = False):
		originalDir = os.getcwd()
		os.chdir(path)
		numExtension = 1
		for i in range(createAmount):
			
			if numExtension == 1 and firstFileStartsAtOne == False:
				numExtension = str(numExtension)
				f = open(keyWord + extensionType, 'w')
			else:
				numExtension = str(numExtension)
				f = open(keyWord + numExtension + extensionType, 'w')
			f.close()
			numExtension = int(numExtension)
			numExtension += 1
		# Return into original directory once complete:
		os.chdir(originalDir)

	#Recursively find and replace file content(Dangerous if not used correctly!):
	def findAndReplaceInFiles(keyWord, replacementKeyword, path, recursive = True):
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
		
	#New version of insert text in file function! (Works very well now unlike pervious version).
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

		# Multiple class folders merging (useful for ML data preprocessing)
	def mergeClassFolders(parentClassPath, mergeDestination, removeOriginal = False):
		# Get the dirs:
		dirs = GatherInfo.readDir(parentClassPath, returnFiles = False)
		# Iterate through each folder in the parentClassPath:
		for folder in dirs:
			# Get the path of the folder:
			folder_path = os.path.join(parentClassPath, folder)
			# Get the files:
			files = GatherInfo.readDir(folder_path, returnDirectories = False)
			#Iterate through each file in the folder:
			for file in files:
				if removeOriginal == False:
					fileOperands.copyFile(os.path.join(folder_path, file), mergeDestination)
				else:
					try:
						fileOperands.moveFile(os.path.join(folder_path, file), mergeDestination)
					except shutil.Error:
						print(f"File \"{os.path.join(mergeDestination, file)}\" already existed before moving file.")

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

	#More reliable functions (reduces chance of directory problems):
	def copyDir(originalDir, newDir):
			lastdir = os.path.basename(os.path.normpath(originalDir))
			newDirectory = os.path.join(newDir, lastdir)
			shutil.copytree(originalDir, newDirectory)
			return True
	def renameFile(newName, filePath):
		#Remove any slash marks:
		newFilePath = os.path.dirname(filePath)
		os.rename(filePath, os.path.join(newFilePath,newName))
		
	def renameDirectory(newName, directoryPath):
		newDirectoryPath = os.path.dirname(os.path.dirname(directoryPath))
		os.rename(directoryPath, os.path.join(newDirectoryPath, newName))
		
     #Create a single file:
	def createFile(fileName, path):
		os.chdir(path)
		f = open(fileName, 'w')
		f.close()
	#Remove a single file:
	def removeFile(filePath):
		os.remove(filePath)

	
	# New in V 2.1.2 (These functions below are all new in V 2.1.2)
	def removeAllFilesInDir(dir, removeDirectories = False):
		directories, files = GatherInfo.readDir(dir)
		for file in files:
			filePath = os.path.join(dir, file)
			os.remove(filePath)
		#Check whether or not the user wants to remove the directories along side the files:
		if removeDirectories == True:
			for directory in directories:
				directoryPath = os.path.join(dir, directory)
				shutil.rmtree(directoryPath)

	# New XOR encryption functions:
	def xor_encrypt_file(file_path, key, removeOriginal = False):
		hashed_key = hashlib.sha256(str(key).encode()).digest()[0]

		with open(file_path, 'rb') as f:
			data = f.read()

		encrypted_data = bytearray(b ^ hashed_key for b in data)  # XOR with hashed_key, not key

		enc_file_path = file_path + '.enc'
		with open(enc_file_path, 'wb') as f:
			f.write(encrypted_data)
		
		if removeOriginal == True:
			os.remove(file_path)

	def xor_decrypt_file(enc_file_path, key, removeEncrypted = False):
		hashed_key = hashlib.sha256(str(key).encode()).digest()[0]
		
		with open(enc_file_path, 'rb') as f:
			data = f.read()

		decrypted_data = bytearray(b ^ hashed_key for b in data)  # XOR with hashed_key, not key

		file_path = enc_file_path.replace('.enc', '')
		with open(file_path, 'wb') as f:
			f.write(decrypted_data)

		if removeEncrypted == True:
			os.remove(enc_file_path)
	
	# Functions that recursivly encrypt/decrypt files
	def xor_encrypt_files(dir, key, removeOriginal = False, recursive = False):
		counter = 0
		for root, dir, files in os.walk(dir):
			if recursive == False and counter != 0:
				break
			for file in files:
				file_path = os.path.join(root, file)
				fileOperands.xor_encrypt_file(file_path, key, removeOriginal=removeOriginal)
			counter += 1
	
	# Note: This function only takes into account files that end with .enc
	def xor_decrypt_files(dir, key, removeEncrypted = False, recursive = False):
		counter = 0
		for root, dir, files in os.walk(dir):
			if recursive == False and counter != 0:
				break
			for file in files:
				if file.endswith(".enc"):
					file_path = os.path.join(root, file)
					fileOperands.xor_decrypt_file(file_path, key, removeEncrypted = removeEncrypted)
			counter += 1
	# Removes all .enc files in a directory recursively:
	def removeEncFiles(dir, recursive = False):
		counter = 0
		for root, dir, files in os.walk(dir):
			if recursive == False and counter != 0:
				break
			for file in files:
				if file.endswith(".enc"):
					file_path = os.path.join(root, file)
					os.remove(file_path)
			counter += 1
		
#The main logging class (Used in Synchronize and Backup classes)
class Logging:
	#Here, the announcement is simply something to announce/thecurrent/main activity or in this case print. dir is the parameter that takes in dir. dirAction consists of things like removing, adding, or copying, renaming, etc.
	def Log(loggingBool, logList, announcement = '', dir1 = '', dir2 = '', dir1Action = '', dir2Action = '', logTag = 'NC', log_non_critical = True):
		#'NC' = Not Critical, 'C' is Critical, for the logTag
		#Check if the boolean loggingBool is True, to determine whether or not the User actually wants to log or not:
		
		if loggingBool == True:
			newLogList = []
			
			#The main log list (which are really the lines that will be passed on to the writeLogsToFile function). This will be returned at the end:

			currentTime = time.ctime()
			
			def printAnnouncement(announcement, currentTime):

				if announcement != '':
					log = f"\n\n[{logTag}] CURRENT/MAIN ACTIVITY:\n{currentTime}: {announcement}\n"
					print(log)
					newLogList.append(log)
			def logDirectories(logList, dir1, dir2, dir1Action, dir2Action, currentTime):
				#First, print the announcement if there is one:
				newLogList = logList
				#Second, print the dir actions:

				#If dir1 is not empty but dir2 is, only print the dir2Action and the dir1:
				if dir1 != '' and dir2 == '':
					log = f"\n	{currentTime}: SUBPROCESS: {dir1Action} {dir1}"
					print(log)
					newLogList.append(log)
				#Vice Versa:
				elif dir1 == '' and dir2 != '':
					log = f"\n	{currentTime}: SUBPROCESS: {dir2Action} {dir2}"
					print(log)
					newLogList.append(log)
				#If they are both included (Something like "Copying files from" = dir1Action, "/path/to/dir1" = dir1, "and putting them into" = dir2Action, "path/to/dir2/" = dir2)
				elif (dir1 and dir2) != '':
					log = f"\n	{currentTime}: SUBPROCESS: {dir1Action} {dir1} {dir2Action} {dir2}" 
					print(log)
					newLogList.append(log)
				
				return newLogList

			#Apply non-critical filter:
			if log_non_critical == False:
				if logTag != 'NC':

					printAnnouncement(announcement, currentTime)
					
					newLogList = logDirectories(newLogList, dir1, dir2, dir1Action, dir2Action, currentTime)
			else:
				printAnnouncement(announcement, currentTime)
					
				newLogList = logDirectories(newLogList, dir1, dir2, dir1Action, dir2Action, currentTime)
		else:
			return logList

		#This logList will be passed by throughout the whole process, and will then be written out to a file after everything is done.
		return newLogList
		

	#The main function to write to the file:
	def writeLogsToFile(creationPath, fileLines, mode):
		#Get the current date:
		currentTime = time.ctime()
		logFileName = f"LogRun({mode})__{currentTime}.txt"
		
		file = os.path.join(creationPath, logFileName)
		#Create and open the log file:
		f = open(file, 'a')
		
		#Write the lines:
		f.writelines(fileLines)
		
		f.close()

#Main Synchronize class:
class Synchronize:
	def backUpToSyncFolder(filePath, syncBackUpFolderName, maindir, syncdir):
		
		#This function returns a path, with an ending including the syncBackUpFolderName:
		def getSyncBackUpFolderPath(maindir, syncdir, syncBackUpFolderName):
			
			#Join the two paths:
			syncBackUpFolderPathMain = os.path.join(maindir, f"{syncBackUpFolderName}")

			syncBackUpFolderPathSync = os.path.join(syncdir, f"{syncBackUpFolderName}")
			return syncBackUpFolderPathMain, syncBackUpFolderPathSync
		
		#Check whether or not the filePath is in the syncBackUpFolder. If it is, dont execute it:
		if syncBackUpFolderName in filePath:
			return False
		#Step 1: retreive the syncBackUpFolderPath
		syncBackUpFolderPathMain, syncBackUpFolderPathSync = getSyncBackUpFolderPath(maindir, syncdir, syncBackUpFolderName)
		
		#Once we have the syncBackUpFolderPath, we can then, copy the file or directory within the parametric filePath variable, and move it to the syncBackUpFolderPath.
		singleComponent = os.path.split(filePath)[1]

		isExistingInSyncBackUpFolderDirectory_Main = os.path.join(syncBackUpFolderPathMain, singleComponent)
		isExistingInSyncBackUpFolderDirectory_Sync = os.path.join(syncBackUpFolderPathSync, singleComponent)

		#If the path leads to a file:
		if os.path.isfile(filePath):
			#Here, check whether or not the file already exists within the syncBackUpFolderPath:

			#Main Path:
			if os.path.exists(isExistingInSyncBackUpFolderDirectory_Main) == True:
				os.remove(isExistingInSyncBackUpFolderDirectory_Main)
			
			fileOperands.copyFile(filePath, syncBackUpFolderPathMain)

			#Sync Path:
			if os.path.exists(isExistingInSyncBackUpFolderDirectory_Sync) == True:
				os.remove(isExistingInSyncBackUpFolderDirectory_Sync)
			
			fileOperands.copyFile(filePath, syncBackUpFolderPathSync)
		
		#If the path leads to a directory:
		if os.path.isdir(filePath):
			#Here, check whether or not the directory already exists within the syncBackUpFolderPath:
			
			#Main path:
			if os.path.exists(isExistingInSyncBackUpFolderDirectory_Main) == True:
				shutil.rmtree(isExistingInSyncBackUpFolderDirectory_Main)
			fileOperands.copyDir(filePath, syncBackUpFolderPathMain)
			
			#Sync path:
			if os.path.exists(isExistingInSyncBackUpFolderDirectory_Sync) == True:
				shutil.rmtree(isExistingInSyncBackUpFolderDirectory_Sync)
			fileOperands.copyDir(filePath, syncBackUpFolderPathSync)
	
	#IMPORTANT: Important files flag is used to never delete certain files that start with a specific character (default = _ ). The importantFilesFlag is important as it may prevent deletion of files/dirs!
	def synchronizeComponents(dir1, dir2, syncBackUpFolderName, syncBackUpFolderExists, importantFilesFlag, loggingBool, maindir, syncdir, log_non_critical = True):
		
		logList = []
		#Checks whether or not the directory or file is important by checking the first character of the string:
		def isImportantFile(dir, importantFilesFlag):

			dir = os.path.basename(os.path.normpath(dir))
			#Get first character and check if it equals importFilesFlag:
			if dir[0] == importantFilesFlag:
				return True
			else:
				return False
		

		#The two very important functions: merge
		def mergeDirectories(parentdir, parentdir2, parentdirs, parent2dirs):
			#For parentdir:
			parentdirHashes = [] 

			#For parentdir2:
			parentdir2Hashes = []

			#First, iterate through parentdir files:
			if len(parentdirs) != 0:
				for dir in parentdirs:
					fullpath = os.path.join(parentdir, dir)
					for folder, dirs, files in os.walk(fullpath):
						os.chdir(folder)
						if len(files) != 0:
							for file in files:
								Hash = GatherInfo.computeHash(file)
								if Hash == False:
									pass
								else:
									parentdirHashes.append(Hash)
			
			#Second, iterate through parentdir2 files:
			if len(parent2dirs) != 0:
				for dir in parent2dirs:
					fullpath = os.path.join(parentdir2, dir)
					for folder, dirs, files in os.walk(fullpath):
						os.chdir(folder)
						if len(files) != 0:
							for file in files:
								Hash = GatherInfo.computeHash(file)
								if Hash == False:
									pass
								else:
									parentdir2Hashes.append(Hash)
			matchBoolean = GatherInfo.isOneInCommon(parentdirHashes, parentdir2Hashes)
			
			return matchBoolean
			
		#The main merge function: Merges the important files and directories together in order to avoid loss of files. Worst case scenario, the deleted files will end up in the syncBackups folder:
		def mergeFiles(parentdir, parentdir2, parentfiles, parent2files):
			#For parentdir:
			parentdirHashes = [] 

			#For parentdir2:
			parentdir2Hashes = []

			#First, iterate through parentdir files:
			if len(parentfiles) != 0:
				for file in parentfiles:
					fullpath = os.path.join(parentdir, file)
					Hash = GatherInfo.computeHash(fullpath)
					if Hash == False:
						pass
					else:
						parentdirHashes.append(Hash)
			
			#Second, iterate through parentdir2 files:
			if len(parent2files) != 0:
				for file in parent2files:
					fullpath = os.path.join(parentdir2, file)
					Hash = GatherInfo.computeHash(fullpath) #Problem lies here:
					if Hash == False:
						pass
					else:
						parentdir2Hashes.append(Hash)
			
			#Now, for the comparison:
			matchBoolean = GatherInfo.isOneInCommon(parentdirHashes, parentdir2Hashes)
			
			return matchBoolean
			#Take in both the parentfiles lists to get the files in each directory. For each of those, create a list with the computed hashes. IF any of those hashes matches any other hash from the other files listed... else...
			#We can return a boolean. True = mathing. False = not matching. Based on this boolean, we can then execute either deleting or merging.
			
		#Main class that takes in dir1, dir2, separates the files and dirs, makes the comparisons, and adds/removes the files, or even renames directories.
		def main(parentdir, parentdir2, syncBackUpFolderName, syncBackUpFolderExists, importantFilesFlag, loggingBool, maindir, syncdir, log_non_critical = log_non_critical):
			
			logList = []
			#Get the source components of the parentdir and parentdir2:
			parentdirs, parentfiles = GatherInfo.readDir(parentdir)
			parent2dirs, parent2files = GatherInfo.readDir(parentdir2)
			
			
			
			#First, do the basic operations:

			#To add files:
			for dir in parentdirs:
				if dir not in parent2dirs:

					newLogList = Logging.Log(loggingBool, logList, announcement = f"Adding directories that exist in mainpath but not in syncpath (missing/extra).", dir1 = f"'{dir}'", dir2 = parentdir2, dir1Action = 'Found directory', dir2Action = f'in {parentdir}, but not in', logTag = "C", log_non_critical = log_non_critical)
					logList.extend(newLogList)
					#If the directory is not in the folder to sync to, then it adds it:
					path = os.path.join(parentdir2, dir)
					os.mkdir(path)
			for file in parentfiles:
				#If the file is not in the folder to sync to, then it adds it
				if file not in parent2files:
					originalpath = os.path.join(parentdir, file)

					newLogList = Logging.Log(loggingBool, logList, announcement = f"Adding files that exist in mainpath but not in syncpath (missing/extra).", dir1 = f"'{file}'", dir2 = parentdir2, dir1Action = 'Found file', dir2Action = f'in {parentdir}, but not in', logTag = 'C', log_non_critical = log_non_critical)
					logList.extend(newLogList)
					fileOperands.copyFile(originalpath, parentdir2)

			#Second, do the hard operations (Merging, replacing with newer versions, important files/dirs)
			
			#Pop out the syncBackUps folder name as to not remove any files or folders from there, if the syncBackUpsFolderExists, of course:
			if syncBackUpFolderExists:
				if syncBackUpFolderName in parentdirs:
					parentdirs.pop(parentdirs.index(syncBackUpFolderName))
				if syncBackUpFolderName in parent2dirs:
					parent2dirs.pop(parent2dirs.index(syncBackUpFolderName))

			#To deal with removing files:
			for file in parent2files:
				if file not in parentfiles:
					
					#Log it:
					newLogList = Logging.Log(loggingBool, logList, announcement = f"Removing additional files:", dir1 = os.path.join(parentdir2, file), dir2 = f'Removing file from {parentdir}', dir1Action = 'File found at ', dir2Action = f'but not found in {parentdir}', logTag = 'C', log_non_critical = log_non_critical)
					logList.extend(newLogList)
					isMatching = mergeFiles(parentdir, parentdir2, parentfiles, parent2files)

					directory = os.path.join(parentdir2, file)

					if isMatching == True or len(parentfiles) < 1:
						
						newLogList = Logging.Log(loggingBool, logList, announcement = "Skipping file and directory merging as some files/dirs are matching.", logTag = 'C', log_non_critical = log_non_critical)
						logList.extend(newLogList)
						#Check if the files are important files. If they are, do not remove them, but rather copy them to the parent dir:
						if isImportantFile(directory, importantFilesFlag) == True:
							#Log it:
							newLogList = Logging.Log(loggingBool, logList, announcement = f"'{directory}' is an important file, as the first character matches the importantFilesFlag. Restoring...", logTag = 'C', log_non_critical = log_non_critical)
							logList.extend(newLogList)

							fileOperands.copyFile(directory, os.path.join(parentdir))
						else:
							
							#If the directory is not in the main directory but is in the sync directory, remove the directory from the sync directory:
							checkDir = os.path.split(directory)[0]
							if os.path.basename(os.path.normpath(checkDir)) == syncBackUpFolderName:
								pass
							else:
								#Check if the user wants a backup folder or not:
								if syncBackUpFolderExists:
									Synchronize.backUpToSyncFolder(directory, syncBackUpFolderName, maindir, syncdir)
								
								#Log it:
								newLogList = Logging.Log(loggingBool, logList, announcement = f"Removing {file} from {parentdir2}, as it doesn't exist in {parentdir}", logTag = 'C', log_non_critical = log_non_critical)
								logList.extend(newLogList)
								os.remove(directory)
					elif isMatching == False:
						#Log it:
						
						#Merge the directories as well:
						for dir in parent2dirs:
							if dir not in parentdirs:
								#Log it:
								newLogList = Logging.Log(loggingBool, logList, announcement = "Merging files and dirs, as no files/dirs are matching.", dir1 = dir, dir2 = f"'{parentdir}'. Merging directories...", dir1Action = "Directory '", dir2Action = f"' exists in {parentdir2}, but not in", logTag = 'C', log_non_critical = log_non_critical)
								logList.extend(newLogList)
								dirDirectory = os.path.join(parentdir2, dir)

								dirDirectoryParent = os.path.join(parentdir, dir)
								
								#Copy the files and the directories:
								if os.path.exists(dirDirectoryParent) == False:
									fileOperands.copyDir(dirDirectory, os.path.join(parentdir))
						
						#Log list:
						newLogList = Logging.Log(loggingBool, logList, announcement = f"Merging missing file: {file} into {parentdir}", logTag = 'C', log_non_critical = log_non_critical)
						logList.extend(newLogList)
						fileOperands.copyFile(directory, os.path.join(parentdir))
			#To deal with directories: (remove from folder to sync to:)
			for dir in parent2dirs:
				if dir not in parentdirs:
					
					#If the directory is not in the main directory but is in the sync directory, remove the directory from the sync directory:


					isMatching = mergeDirectories(parentdir, parentdir2, parentdirs, parent2dirs)
					
					directory = os.path.join(parentdir2, dir)

					if isMatching == True or len(parentdirs) < 1:
						#Log it: CONTINUE HERE
						newLogList = Logging.Log(loggingBool, logList, announcement = "Skipping file and directory merging as some files/dirs are matching.", log_non_critical = log_non_critical)
						logList.extend(newLogList)
						
						#Check if it is important directory:
						if isImportantFile(directory, importantFilesFlag) == True:
							#Log it:
							newLogList = Logging.Log(loggingBool, logList, announcement = f"'{directory}' is an important directory, as the first character matches the importantFilesFlag. Restoring...", logTag ='C', log_non_critical = log_non_critical)
							logList.extend(newLogList)
							
							fileOperands.copyDir(directory, os.path.join(parentdir))
						else:
							#Here check if the directory name before the directory is the synBackUpFolderName. That way, the remove doesnt deal with the synBackUpsFolder:
							checkDir = os.path.split(directory)[0]
							if os.path.basename(os.path.normpath(checkDir)) == syncBackUpFolderName:
								pass
							else:
								#Backup:
								if syncBackUpFolderExists:
									Synchronize.backUpToSyncFolder(directory, syncBackUpFolderName, maindir, syncdir)
								
								#Log it:
								newLogList = Logging.Log(loggingBool, logList, announcement = f"Removing {directory} and all of its contents, as it is directory {parentdir2}, but not in {parentdir}", logTag= 'C', log_non_critical = log_non_critical)
								logList.extend(newLogList)

								shutil.rmtree(directory)
					else:
						
						for file in parent2files:
							if file not in parentfiles:
								fileDirectory = os.path.join(parentdir2, file)
								parentFileDirectory = os.path.join(parentdir, file)

								#Log it:
								newLogList = Logging.Log(loggingBool, logList, announcement = "Merging files and dirs, as no files/dirs are matching.", dir1 = file, dir2 = f"'{parentdir}'. Merging Files...", dir1Action = "File '", dir2Action = f"' exists in {parentdir2}, but not in", logTag = 'C', log_non_critical = log_non_critical)
								logList.extend(newLogList)

								#Copy the files and the directories:
								if os.path.exists(parentFileDirectory) == False:
									fileOperands.copyFile(fileDirectory, os.path.join(parentdir))
						
						#Add a try except block in case the function above this one already took care of the directories:
						try:

							newLogList = Logging.Log(loggingBool, logList, announcement = f"Copying missing dir: {dir}, into {parentdir}", logTag = 'C', log_non_critical = log_non_critical)
							logList.extend(newLogList)

							fileOperands.copyDir(directory, os.path.join(parentdir))
						except FileExistsError:
							pass

				
			#Here, create a for loop similar to those above that actually update the contents of a file by checking the time last modified, removing the old file, and copying the new one.
			for file in parentfiles:
				maindirpath = os.path.join(parentdir, file)
				dirsyncpath = os.path.join(parentdir2, file)

				mainfiletime = os.path.getmtime(maindirpath)

				dirsyncfiletime = os.path.getmtime(dirsyncpath)
				#Compute hashes (hot fix 2.0.4)
				if (GatherInfo.computeHash(maindirpath) != GatherInfo.computeHash(dirsyncpath)):
					if (mainfiletime > dirsyncfiletime):
						#Remove and copy the file:
						os.remove(dirsyncpath)
						fileOperands.copyFile(maindirpath, os.path.split(dirsyncpath)[0])
						newLogList = Logging.Log(loggingBool, logList, announcement = f"Updating file contents:", dir1 = maindirpath, dir2 = "Updating file.", dir1Action = 'File at path', dir2Action = f'was modified before file {dirsyncpath}.', logTag = 'C', log_non_critical = log_non_critical)
						logList.extend(newLogList)
					elif mainfiletime < dirsyncfiletime:
						os.remove(maindirpath)
						newLogList = Logging.Log(loggingBool, logList, announcement = f"Updating file contents:", dir1 = dirsyncpath, dir2 = "Updating file.", dir1Action = 'File at path', dir2Action = f'was modified before file {maindirpath}.', logTag = 'C', log_non_critical = log_non_critical)
						logList.extend(newLogList)
						fileOperands.copyFile(dirsyncpath, os.path.split(maindirpath)[0])
			return logList
		#Execute the main function:		
		newLogList = main(dir1, dir2, syncBackUpFolderName, syncBackUpFolderExists, importantFilesFlag, loggingBool, maindir, syncdir)
		logList.extend(newLogList)
		
		return logList
	#Organize the path slashes, as os.path.join would not always work properly:
	def organizePathSlashes(path):
		if  ("/" or "\\") not in (path[-1]):
			path = path + "/" 
		return path

	#Function to move removed files and folders into in case of accidental deletions:
	def createSyncBackupFolder(dir1, dir2, syncBackUpFolderName):
		os.chdir(dir1)
		if os.path.exists(syncBackUpFolderName) == False:
			os.mkdir(syncBackUpFolderName)

		os.chdir(dir2)
		if os.path.exists(syncBackUpFolderName) == False:
			os.mkdir(syncBackUpFolderName)

	#For synchronizing files and dirs (The main function:)
	def synchronize(dir1, dir2, importantFilesFlag = '_', syncBackUpFolderExists = True, loggingBool = False, logCreationPath = '', log_non_critical = True):
		
		#The main logList:
		logList = []

		#Log it:
		#Check if the user actually wants to create a syncBackUpFolder (It is recommended in order to reduce the chances of accidental file loss!)
		newLogList = Logging.Log(loggingBool, logList, announcement = f"Running in mode SYNCHRONIZATION: importantFilesFlag = '{importantFilesFlag}', syncBackUpFolderExists = {syncBackUpFolderExists}", logTag = 'C', log_non_critical = log_non_critical)
		#Append to the logList
		logList.extend(newLogList)
		#Initialize the backup directory:
		syncBackUpFolderName = f"{importantFilesFlag}syncBackups"
		if syncBackUpFolderExists == True:
			
			#Create the backup Folder:
			Synchronize.createSyncBackupFolder(dir1, dir2, syncBackUpFolderName)
		
		
		#Organize the directory slash marks (to avoid errors)
		dir1 = Synchronize.organizePathSlashes(dir1)
		dir2 = Synchronize.organizePathSlashes(dir2)

		maindir = dir1
		syncdir = dir2
		#Get the time of when the folders were last modified:
		# dir1ti_m = os.path.getmtime(dir1)
		# dir2ti_m = os.path.getmtime(dir2)
		dir1ti_m = []
		dir2ti_m = []

		

		#Check the times in the dir1:
		for folder, dirs, files in os.walk(dir1):
				#Here, get everything that is after the dir1 in order to get the other directories:
				
				time = os.path.getmtime(folder)
				
				#Append the values:
				dir1ti_m.append(time)
				
				#Get the time modified for the files as well:
				if len(files) != 0:
					for i in range(len(files)):

						filePath = os.path.join(folder, files[i])

						fileTimeModified = os.path.getmtime(filePath)

						dir1ti_m.append(fileTimeModified)
		#Now, do the same thing, but check for dir2 for which was last modified:
		for folder, dirs, files in os.walk(dir2):
				
				#Here, get everything that is after the dir1 in order to get the other directories:
				
				timedir = os.path.getmtime(folder)
				
				#Append the values:
				dir2ti_m.append(timedir)

				if len(files) != 0:
					for i in range(len(files)):

						filePath = os.path.join(folder, files[i])

						fileTimeModified = os.path.getmtime(filePath)

						dir2ti_m.append(fileTimeModified)



		dir1time = max(dir1ti_m)
		dir2time = max(dir2ti_m)

		#Log it:
		newLogList = Logging.Log(loggingBool, logList, announcement = f"Recursively got the time last modified for each directory: {dir1time} for {dir1} and {dir2time} for {dir2}", log_non_critical = log_non_critical)
		#Append to the logList
		logList.extend(newLogList)

		#The greater (bigger) time indicates the folder that was edited most recently:
		if float(dir1time) > float(dir2time):
			#IMPORTANT: Here, place if statement, deciding which folder was edited last (In other words, decide which one should follow the other based on the time they were edited. The one that gets edited the most recent gets the priority)
			#When doing the above, invert the dir1 with dir2 (Because you are doing pretty much the opposite!)
			for folder, dirs, files in os.walk(dir1):
				#Here, get everything that is after the dir1 in order to get the other directories:
				
				childdir = (folder.split(dir1,1)[1])
				
				syncpath = os.path.join(dir2, childdir)

				newLogList = Logging.Log(loggingBool, logList, announcement = f"Iterating through main loop with {dir1} as the main dir, as {dir2} has an older modification time.", dir1 = folder, dir2 = syncpath, dir1Action = 'Entering child directory', dir2Action = "to compare files and dirs with ", log_non_critical = log_non_critical)
				#Append to the logList
				logList.extend(newLogList)
				
				#Set the newLogList equal to the log that the function returns:
				newLogList = Synchronize.synchronizeComponents(folder, syncpath, syncBackUpFolderName, syncBackUpFolderExists, importantFilesFlag, loggingBool, maindir, syncdir, log_non_critical = log_non_critical)
				logList.extend(newLogList)

		elif float(dir1time) < float(dir2time):
			for folder, dirs, files in os.walk(dir2):
				#Here, get everything that is after the dir1 in order to get the other directories:
				childdir = (folder.split(dir2,1)[1])
				syncpath = os.path.join(dir1, childdir)

				newLogList = Logging.Log(loggingBool, logList, announcement = f"Iterating through main loop with {dir2} as the main dir, as {dir1} has an older modification time.", dir1 = folder, dir2 = syncpath, dir1Action = 'Entering child directory', dir2Action = "to compare files and dirs with ", log_non_critical = log_non_critical)
				#Append to the logList
				logList.extend(newLogList)

				#Set the newLogList equal to the log that the function returns:
				newLogList = Synchronize.synchronizeComponents(folder, syncpath, syncBackUpFolderName, syncBackUpFolderExists, importantFilesFlag, loggingBool, maindir, syncdir, log_non_critical = log_non_critical)
				
		
				logList.extend(newLogList)
		#At the very end, check if loggingBool is True. If it is, write the lines of the list logList to the specific directory of where the Log should be created:
		if loggingBool == True:
			#Write logs to file:
			Logging.writeLogsToFile(logCreationPath, logList, 'synchronize')
			
#Class Backup: Unlike synchronization, this backs up to a 'child' directory, meaning that the 'child' directory plays no role on the parent one.
class Backup:
	#Capture the newLogList from the mainIteration function:
	def main(parentmaindir, childbackupdir, loggingBool, log_non_critical = True):
		
		
		
		#Define the main loglist to append to:
		logList = []
		
		
		#Get the source components of the parentdir and childsyncdir (in order to compare them later:)
		
		maindirs, mainfiles = GatherInfo.readDir(parentmaindir)
		syncdirs, syncfiles = GatherInfo.readDir(childbackupdir)
		
		#Log it:
		newLogList = Logging.Log(loggingBool, logList, announcement = "Reading directories and files in the listed directories:", dir1 = parentmaindir, dir2 = childbackupdir, dir2Action = ',', log_non_critical=log_non_critical)
		#Append to the logList
		logList.extend(newLogList)
		
		#To add files:
		for dir in maindirs:
			if dir not in syncdirs:
				#If the directory is not in the folder to sync to, then it adds it:

				#Log it:
				newLogList = Logging.Log(loggingBool, logList, announcement = "Adding missing directories in the backup folder(s): ", dir1 = parentmaindir, dir2 = childbackupdir, dir1Action = f"Dir '{dir}' found in", dir2Action = 'but not found in', logTag = 'C', log_non_critical=log_non_critical)
				#Append to the logList
				logList.extend(newLogList)

				path = os.path.join(childbackupdir, dir)
				os.mkdir(path)
		for file in mainfiles:
			#If the file is not in the folder to sync to, then it adds it:
			if file not in syncfiles:
				filepath = os.path.join(parentmaindir, file)

				newLogList = Logging.Log(loggingBool, logList, announcement = "Adding missing files in the backup folder(s): ", dir1 = parentmaindir, dir2 = childbackupdir, dir1Action = f"File '{file}' found in", dir2Action = 'but not found in', logTag = 'C', log_non_critical=log_non_critical)
				#Append to the logList
				logList.extend(newLogList)

				fileOperands.copyFile(filepath, childbackupdir)

		#To remove files (remove from folder to sync to:)
		for dir in syncdirs:
			if dir not in maindirs:
				
				#Log it:
				newLogList = Logging.Log(loggingBool, logList, announcement = "Removing extra directories in the backup folder: ", dir1 = parentmaindir, dir2 = childbackupdir, dir1Action = f"File '{file}' not found in", dir2Action = 'but found in backup folder. Removing from backup Folder:', logTag = 'C', log_non_critical=log_non_critical)
				#Append to the logList
				logList.extend(newLogList)
				#If the directory is in the backup directory but not in the main dir, remove the dir from the backup (sync) directory:
				directory = os.path.join(childbackupdir, dir)
			
				
				shutil.rmtree(directory)
		
		#Remove the file from the 
		for file in syncfiles:
			if file not in mainfiles:
				
				#Log it:
				newLogList = Logging.Log(loggingBool, logList, announcement = "Removing any extra files in the backup folder: ", dir1 = parentmaindir, dir2 = childbackupdir, dir1Action = f"File '{file}'not found in", dir2Action = 'but found in backup folder. Adding removing from backup Folder:', logTag = 'C', log_non_critical=log_non_critical)
				logList.extend(newLogList)
				
				#If the backup directory has the file but the main one doesn't, remove it from the backup directory:
				os.remove(os.path.join(childbackupdir, file))	

		#Use this to update file content:
		for file in mainfiles:
				maindirpath = os.path.join(parentmaindir, file)
				dirsyncpath = os.path.join(childbackupdir, file)

				mainfiletime = os.path.getmtime(maindirpath)

				dirsyncfiletime = os.path.getmtime(dirsyncpath)

				#If the file needs to be updated, remove the old one and copy the new one to the backup folder:
				if (GatherInfo.computeHash(maindirpath) != GatherInfo.computeHash(dirsyncpath)):
					if mainfiletime > dirsyncfiletime:
						#Remove and copy the file:
						os.remove(dirsyncpath)
						fileOperands.copyFile(maindirpath, os.path.split(dirsyncpath)[0])
					
						newLogList = Logging.Log(loggingBool, logList, announcement = f"Updating content of file '{file}'", dir1 = dirsyncpath, dir2 = maindirpath, dir1Action = "Updating file content at '", dir2Action = f"' as file '{file}' in backup folder is older than", logTag = 'C', log_non_critical=log_non_critical)
						logList.extend(newLogList)
		
		#At the end of the main() function, return the logList
		return logList
	def mainIteration(maindir, backupdir, loggingBool, log_non_critical = True):
		
		logList = []
		for folder, dirs, files in os.walk(maindir):
			
			childdir = (folder.split(maindir,1)[1])
			#Replace the first slash:
			try:
				if childdir[0] == "/" or childdir[0] == "\\":
					childdir = childdir[1:]
			except:
				pass
			backupdir = Synchronize.organizePathSlashes(backupdir)
			#Here, the very start is blank because the childdir is blank (Perhaps, just leave it as is? It does not really matter)
			backUpFullPath = os.path.join(backupdir, childdir)
			#Log it:
			newLogList = Logging.Log(loggingBool, logList, announcement = "Entering main loop under mainIteration function", dir1 = childdir, dir2 = backUpFullPath, dir1Action = "Merged child path string '", dir2Action = "' into sync path:", log_non_critical=log_non_critical)
			logList.extend(newLogList)
			
			#Transfer the newLogList to the main() function:

			logListMain = Backup.main(folder, backUpFullPath, loggingBool, log_non_critical = log_non_critical)

			logList.extend(logListMain)
		
		#Return the logList, which is the file lines to write:
		return logList
	def backup(maindir, backupdirs, loggingBool = False, logCreationPath = '', log_non_critical = True):
		#Initialize the main logList:
		logList = [] 
		
		newLogList = Logging.Log(loggingBool, logList, announcement = "Running in BACKUP mode:", logTag = 'C', log_non_critical=log_non_critical)
		
		logList.extend(newLogList)
		
		
		if isinstance(backupdirs, list) != True:
			raise Exception("ERR: 'backupdirs' must be of type 'list'")
		
		#For every dir within the backup directories, backup:
		for dir in backupdirs:
			if len(backupdirs) > 1:
				newLog = Logging.Log(loggingBool, logList, announcement = f"Multiple Directories were given. Now, backing up to directory: {dir}", log_non_critical=log_non_critical)
				logList.extend(newLog)
			newLogList = Backup.mainIteration(maindir, dir, loggingBool, log_non_critical=log_non_critical)
			logList.extend(newLogList)
		#Write the logs:
		
		if loggingBool == True:
			Logging.writeLogsToFile(logCreationPath, logList, 'backup')
	def backgroundBackup(maindir, backupdirs, loggingBool = False, logCreationPath = '', refreshInterval = 8, log_non_critical = True):

		#Now, implement logging in the synchronization algorithm.
		modeAnnounced = False
		while True:
			logList = []
			if modeAnnounced == False:
				newLogList = Logging.Log(loggingBool, logList, announcement = "Running in BACKGROUNDBACKUP mode:", logTag = 'C', log_non_critical=log_non_critical)
				logList.extend(newLogList)
				modeAnnounced = True
			
			for dir in backupdirs:
				
				if len(backupdirs) > 1:
					newLog = Logging.Log(loggingBool, logList, announcement = f"Multiple Directories were given. Now, backing up to directory: {dir}", log_non_critical=log_non_critical)
					logList.extend(newLog)
				newLogList = Backup.mainIteration(maindir, dir, loggingBool, log_non_critical=log_non_critical)
				logList.extend(newLogList)
				#Write the logs to a file:
			if loggingBool == True:
				Logging.writeLogsToFile(logCreationPath, logList, 'backgroundBackup')
			time.sleep(refreshInterval)
			
#Call a bash/shell script:
class callBash:
	def runFile(path, editPermissions = False):
		#If edit permissions is set to true, edit the permission (to avoid permission errors)
		if editPermissions == True:
			os.system("chmod +x " + path)
		subprocess.run([path], shell = True)