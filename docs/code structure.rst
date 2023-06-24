.. _code structure:

***************
Code Structure
***************

In the code, there are six classes:::

	GatherInfo

	fileOperands

	Logging

	Synchronize

	Backup

	callBash

.. note::

	The 'Logging' class is not important to the user and is therefore not imported within the package. It is solely used by the Synchronize and Backup classes.


The **GatherInfo** class
========================

The **GatherInfo** class consists of many different functions to gather general info on files and directories.

The ``getAmountofFilesinDir`` Function:
----------------------------------------

This function iterates through all files and directories in a directory, and checks whether or not the location is a file or a directory. If it is a file, then it adds a value of 1 to a counter. When the function ends, it returns the value of the counter.

The ``getAllFileNamesinDir`` Function:
----------------------------------------

This function is simply another way of executing the ``os.listdir`` command. It returns all files and directories in a specific path.

The ``expandListInfo`` Function:
--------------------------------

This function works by iterating through a given list, and printing each element in the structure of column. In other words, it simply displays any list in a spread out form, and is there to print out information.

The ``getFileLineContents`` Function:
-------------------------------------

This function works by opening a given file, and reading its lines with the f.readlines() function provided by Python. It then returns the lines in the form of a list.

The ``getFileLineAmount`` Function:
-------------------------------------

This function works very similarly to the ``getFileLineContents``, but instead of returning the actual file lines, it returns the amount of lines by using the len() function provided by Python, which is used on the lines list.

The ``isEmptyDir`` Function:
----------------------------

This function returns a boolean of either True of False. It works by taking in any directory as its path, and lists the directories in the directory. If the list of directories is 0, then it is True. Else, it is false.

The ``computeHash`` Function:
-----------------------------

This function uses the hashlib library in order to function properly. It takes in any file as its path, opens the file, and returns a digest of the file by examining the contents of the file.

The ``isOneInCommon`` Function:
-------------------------------

This function takes in any two lists. It then iterates through each list, gets an instance of each element within the list, and compares that element to all the other elements in the other list.

The ``readDir`` Function:
-------------------------

The readDir is a very important function that is used throughout the FinderZ library. It has the option to return the files or directories in a path, or even both, in the form of a list. It works by creating two lists for files and directories, iterating through the files list of the path, and checking whether or not it is a file or a directory. Based on the result, it then appends it to the according list.

The ``getTotalInfo`` Function:
------------------------------

This function works by intancing two variables, one for file lines, and another for files. Its purpose is to rescurisvely go through every file in a directory and scan the amount of lines it has. It then returns that amount, and also can return the total amount of files that it iterated through.

Thanks to the os.walk() function, recusrive actions are very easy to do, which what makes this possible along with many other recursive actions within other functions.


The **fileOperands** class
==========================

The **fileOperands** class is the main class that contains many useful functions for various file operations. In V2, so many new things are added and fixed. Go check out the :doc:`updatev2` for more information on the V2 update of FinderZ!

* findFiles
* scanFilesForContent
* removeFiles
* createFiles
* findAndReplaceInFiles
* insertTextInFile
* moveFile
* copyFile
* moveDir
* copyDir
* renameFile
* renameDirectory
* createFile
* removeFile

.. note::

	Each of these functions above have a variety of different options. You can refer to the :doc:`function use` section of the documentation to find out how to use them.


The ``findFiles`` Function:
---------------------------

This is a function that can be used to find files in a directory. There are different methods and options regarding the searching, but that will be referred to in the :doc:`function use` section of this guide. 

Regarding how the actual function works, it iterates through every file in a directory, and finds the files that either contain or exactly match a file and its name. Once the file is found, it appends the path to the file to a list, which the function then returns as a value.

The ``scanFilesForContent`` Function:
-------------------------------------

This function works by going through every file in a directory, opening the file, and reading its lines. For each lines, it scans for the given keyword that was inputted into the function. If the keyword is found, it appends the file path to a list, which is what will be returned by the function as a value.

The ``removeFiles`` Function:
-----------------------------

This function makes it easy to remove files with a specific keyword, or even a general keyword, and works by adding user interaction in confirming whether or not to delete the files containing/matching the keyword in their name. It can either recursively search and remove files, or just remove files in a specified directory.

The ``createFiles`` Function:
-----------------------------

This function works by taking in the amount of files to create. It then creates a for loop, which then creates a file for every iteration to the path that was inputted in. 

The ``findAndReplaceInFiles`` Function:
---------------------------------------

This function is not like any other find and replace function that replaces keywords in a specific file. Instead, it replaces a certain keyword throughout every file, with a recursive option as well, which is listed for each directory. It works by reading every (decodable) file and its lines, and then scanning (and replacing) the keyword with a replacement keyword.

The ``insertTextInFile`` Function:
----------------------------------

This function is one of the more complex of functions. This is due to a file having new lines, which misplaces the exact line number. Because of this,a place holder was appended at the start to the file lines list, which could then be used to avoid new line issues. It even has an appendNewLines option, which works by continiously adding new lines until the given amount is reached. the append new linse option can be used to write to a line number that is larger than the total amount of lines that the file has in the first place.

.. note::
	
	Concerning the smaller functions, such as moving directories, copying files, etc., those functions are very simple and need no explanation. These mostly use the os library in order to execute their jobs.


The **Logging** class
==========================

The **Logging** class consists of logging functions used in the **Synchronize** and **Backup** classes. It consists of functions that can take in parameters in order to construct detailed sentences in order to have detailed logs. The main purpose of the **Logging** class is to create logs of the actions of the **Synchronize** and **Backup** classes, as anything that may go wrong while using those classes can be recovered.

It consists of two functions, ``Log`` and ``writeLogsToFile``. ``writeLogsToFile`` consists of taking in a list, which represents file lines, and then writes them to a file. The ``Log`` function takes in a lot of parameters, and is used to construct detailed logging in the form of a sentence. The **Logging** class has no use for the user, but is rather used by the **Synchronize** and **Backup** classes. 

The **Synchronize** class
==========================

.. note::

	The **Synchronize** class consists of one main function, ``synchronize``. So, this section of this guide, as well as the :doc:`function use` section of this guide, will only cover the ``synchronize`` function, and the sub functions that it calls.

The ``synchronize`` Function:
-----------------------------

The ``synchronize`` function is the main parent function for file synchronization. In order to find out more about this, refer to the :ref:`synchronize function use` section of this guide.

The synchronize function is constructed in a way that first takes in two directories to synchronize, gets the time of the directories last modified, and whoever was modified last, follows that directory in terms of actions. It then calls a sub function called synchronizeComponents, which then calls the main() function within the synchronizeComponents function. The main() function includes all of the synchronization algorithms, which then call other functions.

The **Backup** class
===================

The **Backup** class consists of a ``main()`` function, which is then called from a ``mainIteration`` function. The ``mainIteration`` function consists of the main recursive loop that then inputs the current path into the ``main()`` function, and the ``main()`` function then executes an algorithm to backup everything that is either missing or is extra. 

The ``backup`` Function:
------------------------

This is the main function that will call the ``mainIteration`` function, and is what the user will be using. More info under the :doc:`function use` section of this guide.

The **callBash** class
=====================

The ``runFile`` Function:
-------------------------

This function works by calling the ``os.system`` command. It then runs a command to run a shell script at the inputted path.