# FinderZ
A library that extends file management functionality in Python with many useful features in order to save your time and make life easier!

![finderz-logo](https://user-images.githubusercontent.com/116693779/213965405-6b416655-09d6-4ef1-ae05-58c32035541d.png)

<p align="center">
	<img src="https://img.shields.io/badge/License-GPL--3.0-brightgreen"
		height="23">
	<img src="https://img.shields.io/badge/Creator-PatzEdi-brightgreen"
		height="23">
	<img src="https://img.shields.io/badge/Latest%20Version-V%201.0-brightgreen"
		height="23">
</p>

FinderZ is now on PyPi! [Check it out here!](https://pypi.org/project/FinderZ/)

This script uses the os and subprocess libraries in order to function properly. 

## **Written in python, this script provides you with different file operation commands as well as info gathering commands on directories as well as files.** 
____________________________________________________________________________
## **CHANGELOG:**
- Added new functions in the GatherInfo class for reading a file and going in depth with its contents.
- Added one new function in the fileOperands class that searches for files with a specific keyword in their content. This function returns the directory of that file.

## **Installation**

Install with PIP:
```
pip3 install FinderZ
```
## **Usage**
Importing:
```
from FinderZ import FinderZLib
```
Example for finding files with a specific keyword:
```
FinderZLib.fileOperands.findFile("fileName", "Custom Directory")
```
Or, if you want to import a single class:
```
from FinderZ.FinderZLib import fileOperands as fO

#Find the file, calling the command "fO":
print(fO.findFiles("fileName", "Custom Path"))
```
## **Features**
- Consists of three classes: GatherInfo, fileOperands, and callBash.
- Find any file with a certain keyword. This means you no longer have to necessarily know the full name of the file in case you forgot it. 
- Gather information such as files in a directory, name of those files, and even a createFiles tool as well as a curated removeFiles tool.
- Is easy to add new things to the library.
- In case of functionality restrictions, callBash is a function that calls a bash script in order to expand functionality at its peak.
- Easy to use.
- You no longer have to take your time in making those file management algorithms that take a while to complete.
- Fast and efficient, includes a plethora of other features. 
____________________________________________________________________________
## **Why?**
- I wanted to showcase how one can easily create a full library that manages files in order to save time in an efficient way. 
- Who wouldn't want a tool to manage their files easily in their python scripts? This will save time!
____________________________________________________________________________
## **How?**
- Using iterating techniques for a few of the functions, I was able to complete actions recursively through different directories. 
- The use of the os and subprocess modules (especially os) made everything easier, and what I did was basically structure a library to make life easier.
____________________________________________________________________________
## **User notice**
- Some of the functions are only there in case one has to get user input or wants to format things in a more visible way. These functions include askMainDir, and the expandListInfo functions.
____________________________________________________________________________
## **Services used (Credits):**
- [OS module](https://docs.python.org/3/library/os.html)
- [Subprocess module](https://docs.python.org/3/library/subprocess.html)
____________________________________________________________________________
## **Make sure to leave a star!**
- If you like this project, leaving a star is what motivates me in doing more. Thank you, and I hope this is useful to all.
