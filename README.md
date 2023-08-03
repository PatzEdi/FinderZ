# FinderZ

Full File Management Library for Python. And growing (V2 is out!)

![logo-color](https://github.com/PatzEdi/FinderZ/raw/main/logo/logo-color.jpg)

<p align="center">
	<img src="https://img.shields.io/badge/License-GPL--3.0-brightgreen"
		height="23">
	<img src="https://img.shields.io/badge/Creator-PatzEdi-brightgreen"
		height="23">
	<img src="https://img.shields.io/badge/Version-Latest-brightgreen"
		height="23">
	
	
</p>
<p align = "center">
	<img src="https://static.pepy.tech/badge/finderz"
		height="23">
</p>

## IMPORTANT: 
**V2 is finally out! To check out the details, go to the readthedocs documentation under the update v2 section!**
**Documentation: [FinderZ](https://finderz.readthedocs.io/en/latest/index.html)** 

**If you want to use the Synchronization and Backup classes, please read the documentation linked above in order to prevent data loss**

**AND: Huge thank you to [@RichardDally](https://github.com/RichardDally) , [@mikudae](https://github.com/mikudae) , [@kyzsuukii](https://github.com/kyzsuukii) , and [@fablau](github.com/fablau) for starring FinderZ.**
## **Written in python, this library provides you with different file operation commands as well as info gathering commands on directories as well as files.** 
____________________________________________________________________________
## **CHANGELOG: V2.0.0**

To check out the details of V2, go to the [documentation](https://finderz.readthedocs.io/en/latest/index.html). This is a big update with many new things!

**Minor Fix Version 2.0.5:**
1. Added log_non_critical parameter in the Synchronize and Backup class functions. If put to False, only critical actions will be displayed, resulting in a minimized log.
2. Fixed file updating in Backup class by adding hash computation to the backup function when updating files. This was already in the Synchronize class.
3. Fixed the Backup directories error (I thought this was already fixed before, but it is totally fixed now.)

**Minor Fix Version 2.0.4:**
- Fixed bug where removing more than one file at a time gave an existence error. Sorry for that!
- Fixed bug where removing a folder that contained folder with the same name as the sync backup folder would result in an infinite loop of backup folders being created.
- Minimized logging by making file updating hash-dependent. Now, updating files is marked as a critical (C) action in the log.
- Removed unnecessary printing in some functions.
- Added a file comparison function in GatherInfo
- Currently, after having tested FinderZ on Android, permission errors may occasionally occur. This is likely due to read/write permissions assigned to a specific file.

**Minor Fix Version 2.0.3:**
- Fixed bug in Backup class that gave an existence error. Sorry about that!
- I have noticed some accidental printing in some functions (such as findFiles, that prints a boolean at the start). This does not currently affect anything, but just prints out occasional, unnecessary output. This will be fixed very soon.
- Thank you for 16K Downloads!

## **Usage**
Installation:
```
pip3 install FinderZ
```
Importing:
```
import FinderZ
```

## **Features**
- Consists of five classes: GatherInfo, fileOperands, Synchronize, Backup, and callBash.
- Advanced file operations, already built for you (including many options to choose from!) 
- Supports regex operations for some functions, as well as specific filters and multiple other choices to choose from. Options such as exact search or something even just containing a keyword, or even having the option to choose to search recursively, are all included.
- Includes full-featured, reliable synchronization and backup classes (beta). Both include optional and detailed logging.
- Full set of info gathering tools under the GatherInfo class.
- Full-featured documentation to guide you through each function in detail. 
- In case of functionality restrictions, callBash is a function that calls a bash script in order to expand functionality at its peak.
- Easy to use.
- You no longer have to take your time in making those file management algorithms that take a while to complete.
- Fast and efficient, includes a plethora of other features. 
____________________________________________________________________________
## **Why?**
- FinderZ is a way to easily expand on the file system of many operating systems. It supports, MacOS, Windows, Linux, and Android.
- Who wouldn't want a tool to manage their files easily in their python scripts? This will save time!
____________________________________________________________________________
## **How?**
- FinderZ is composed of many iterating techniques and parametric options. Based on these options, the core of each function deals with a user's choice of what to do or what not to do.
- More info under the documentation!
____________________________________________________________________________
## **User notice**
- I am not responsible for any damage or data lost using the FinderZ library. 
- If using the Synchronize class, make sure renaming files or directories is never the last thing you do before synchronization, unless it is the only thing you did do (no adding, removing, copying, etc. files before)
- This project has just been released to version 2! It has grown so much, but it is still growing and improving.
____________________________________________________________________________
## **Services used (Credits):**
- [OS module](https://docs.python.org/3/library/os.html)
- [Shutil module](https://docs.python.org/3/library/shutil.html)
- [Time module](https://docs.python.org/3/library/time.html)
- [Hashlib module](https://docs.python.org/3/library/hashlib.html)
- [re](https://docs.python.org/3/library/re.html)
- [Subprocess module](https://docs.python.org/3/library/subprocess.html)

____________________________________________________________________________
## **Make sure to leave a star!**
- If you like this project, leaving a star is what motivates me in doing more. Thank you, and I hope this is useful to all.
