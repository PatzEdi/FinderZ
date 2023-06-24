import shutil
import os

#For dealing with files:

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

#VERSION 1.2.0
def renameFile(newName, filePath):
	#Remove any slash marks:
	newFilePath = os.path.dirname(filePath)
	os.rename(filePath, newFilePath + "/" + newName)
	
def renameDirectory(newName, directoryPath):
	newDirectoryPath = os.path.dirname(os.path.dirname(directoryPath))
	os.rename(directoryPath, newDirectoryPath + "/" + newName)

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
				

#insertTextInFile("Insertion", 2, "/Users/edwardferrari/MyPythonProjects/GitHubRepos/insertion.txt", appendNewLines = False)