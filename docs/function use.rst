.. _function use:

*************
Function Use
*************

.. note::
    
    The Function Use section of the documentation is the biggest section present. It presents detailed information about each function and what the user can do.

Importing
=========

If you want to import the full library:

.. code-block:: python

    import FinderZ


**IMPORTANT: For the purpose of this part of the documentation, we will be importing the library like so:**

.. code-block:: python

    from FinderZ import GatherInfo
    from FinderZ import fileOperands
    from FinderZ import Synchronize
    from FinderZ import Backup
    from FinderZ import callBash


The reason we do this is to simplify everything without having to call FinderZ every time.

**GatherInfo** Usage
====================

.. note::
    
    The functions that will be explained will be explained upon how they can be used. There will be frequent use of printing the variable which stores the output of these functions. The printing is solely there in case you want to try the code for yourself and see the output.

``getAmountofFilesinDir``
-------------------------

The ``getAmountofFilesinDir`` function is used in order to get the total amount of files in a directory. It only counts files and not directories.

It takes in one required parameter: dir path (str)

In order to use it, you can set the execution of the function equal to a variable, which stores a value of type int.

.. code-block:: python

    amountFiles = GatherInfo.getAmountofFilesinDir('/path/to/dir') #Replace /path/to/dir with a path to a directory. 
    print(amountFiles)

The above code stores the integer value in the variable amountFiles, and then prints it out. 

``getAllFileNamesinDir``
------------------------

The ``getAllFileNamesinDir`` function is a function that is used many times throughout the library. It is used in order to get a list of files (including directories) in a specific path.

It takes in one required parameter: dir path (str)

The function returns a list, so you can set the function equal to a variable, which will be of type list, like so:

.. code-block:: python

    files = GatherInfo.getAllFileNamesinDir('/path/to/dir') #Replace /path/to/dir with a path to a directory. 
    print(files)

The above code stores a list of files (directories included!) into the files variable, then prints it out. 

``expandListInfo``
------------------

The ``expandListInfo`` function is used in order to print a list and its contents in consecutive, vertical form. It has no use in the library itself, but can be used in order to display a list in a more readable form.

It takes in one required parameter: list (list)

You can input any list, and it prints out the contents for you.

``getFileLineContents``
-----------------------

The ``getFileLineContents`` function is an important function that is used throughout the FinderZ library. It returns the lines of a file in the form of a list.

It takes in one required parameter: file path (str)

You can use the function like so:

.. code-block:: python

    fileLines = GatherInfo.getFileLineContents('/path/to/file') #Replace /path/to/file with a path to a file. 
    print(fileLines)

The above code will store the file lines in the fileLines variable in the form of a list, and print them out. 

``getFileLineAmount``
---------------------

The ``getFileLineAmount`` function is used in order to get the exact amount of lines in a file. 

It takes in one required parameter: file path (str)

You can use it like so:

.. code-block:: python

    lineAmount = GatherInfo.getFileLineAmount('/path/to/file') #Replace /path/to/file with a path to a file. 
    print(lineAmount)

The above code stores the amount of lines in the form of an integer in the variable lineAmount, and then prints it.

``isEmptyDir``
--------------

The ``isEmptyDir`` function is used in order to check whether or not a directory is empty. It returns a boolean value: True if empty, False if not empty.

It takes in one required parameter: dir path (str)

The function can be used by storing the boolean in a variable like so.

.. code-block:: python

    isEmptyDir = GatherInfo.isEmptyDir('/path/to/dir') #Replace /path/to/dir with a path to a dir. 
    print(isEmptyDir)

The above code will print a boolean value, which is stored in the isEmptyDir variable.

``computeHash``
---------------

The ``computeHash`` function is used in order to get the hash value of a file. It stores the value as a string. 

It takes in one required parameter: file path (str)

You can use the function like so:

.. code-block:: python

    hash = GatherInfo.computeHash('/path/to/file') #Replace /path/to/file with a path to a file. 
    print(hash)

The above code stores the hash value in the hash variable and prints it out after. (Again, as a reminder, the printing is not needed of course, it is just there to show the output.)

``isOneInCommon``
-----------------

The ``isOneInCommon`` function is used to check whether or not two functions have at least one item in common. This function is primarily used by the library, unless the user wants to use it for other purposes.

It takes in two required parameters: list1, list2 (lists)

The function returns a boolean and can be used like so:

.. code-block:: python

    isOneInCommon = GatherInfo.isOneInCommon(list1, list2)
    print(isOneInCommon)

The above code checks whether or not the two lists have at least one element in common. The boolean is stored in the isOneInCommon variable, and is then printed.

``readDir``
-----------

The ``readDir`` function is one of the most important functions under the **GatherInfo** class.

It takes in one required parameter: dir path (str)

It takes in two optional parameters: returnFiles, returnDirectories (booleans)

The function returns either files or directories depending on the options returnFiles and returnDirectories. If returnFiles is False, it only returns directories, and vice versa.

The function can be used like so, if both files and directories are returned:

.. code-block:: python

    directories, files = GatherInfo.readDir('/path/to/dir/') #Replace /path/to/dir with a path to a dir.
    print(files, directories)

The above code stores the directories and files into two separate variables, and then prints both of them.

If you want to only return files and not return directories, you can do so like this:

.. code-block:: python

    files = GatherInfo.readDir('/path/to/dir/', returnDirectories = False) #Replace /path/to/dir with a path to a dir.
    print(files)

If you want to only return directories and not return files, you can do the same thing, but with returnFiles = False. It is the same thing as the above, but opposite.

``isRegexAndStringMatching``
----------------------------

The ``isRegexAndStringMatching`` function is used by the library, but can be used by the user as well for other purposes.

The main purpose of this function is to determine whether or not a regex pattern matches (either within or exactly) a string. 

It takes in two required parameters: pattern, string (str)

It takes in one optional parameter: exactMatch (boolean)

The exactMatch parameter is in a boolean type. If set to true, the function will return whether or not the pattern exactly matches the string. Otherwise, the function only checks if the string includes the pattern rather than matching it completely.

The function can be used like so:

.. code-block:: python

    matching = GatherInfo.isRegexAndStringMatching('pattern', 'string') #Replace pattern with a valid regex pattern.
    print(matching)

The above code stores a boolean value in the variable matching, and prints it. If you want to check whether or not the string exactly matches the pattern, include the exactSearch = True parameter when calling the function.

``getTotalInfo``
----------------

The ``getTotalInfo`` function is used in order to get the total number of lines, and optionally even files, recursively or not recursively, within a directory.

It takes in one required parameters: path (str)

It takes in three optional parameters: returnFileAmount (boolean), extensionFilters (list), recursive (boolean)

The returnFileAmount determines whether or not to return the total amount of files that were iterated through. 

In case you only want to scan and include files with specific file extensions, you can define them in the extensionFilters parameter.

If you want to count all files and their lines recursively, set the recursive option equal to True.

In the end, the whole function with all properties would look like this, but you can modify it as you wish, of course:

.. code-block:: python

    lines, files = GatherInfo.getTotalInfo('pattern', 'string', returnFileAmount = True, extensionFilters = ['.py'], recursive = True) #Replace pattern with a valid regex pattern.
    print(lines, files)

The above code takes in .py (python files) only, as we have added .py in the file extension filter list. **Keep in mind, you can add as many extensionFilters as you want** which is why it is in the form of a list.

The recursive option is set to true, so it will scan every (Python) file recursively in each directory, and files are returned with the returnFileAmount parameter set to True.

**fileOperands** Usage
======================

The **fileOperands** class contains the biggest functions in the library. These functions are special functions which can be of use fo many users.

``findFiles``
-------------

The ``findFiles`` function is used in order to find files. It has many different options:

It takes in two required parameters: fileName (str), dir path (str)

It takes in three optional parameters: exactSearch (boolean), recursive (boolean), regex (boolean)

The function returns a list of the paths of the files that it finds with the matching inputted keyword, denoted by fileName.

The exactSearch parameter can be used if you want to find files with the exact form as the keyword (yes, this does include the extension!). If left to a default of False, the function will search for files with their names containing the keyword, rather than exactly matching it.

The recursive option is a boolean. If set to true, it will search recursively. 

The regex option can be used if you want to find files with more specific names. If you want to use regex, you can set the regex parameter to True, and use a valid regex pattern in the fileName parameter, in the form of a string.

In order to use the findFiles function, you can do so like this:

.. code-block:: python

    files = fileOperands.findFiles('keyword', '/path/to/dir', recursive = True) #Replace keyword with your own key word, /path/to/dir with a path to a dir.
    print(files)

The above code will recursively scan the given path for files that contain (not exactly match!) the keyword in their names. 

Once that is done, it returns a list, in this case stored in the variable files, which contains the paths to each file containing that keyword.

If you want to use regex, you can do so like this:

.. code-block:: python

    files = GatherInfo.findFiles('foo[dt]', '/path/to/dir', recursive = True, regex = True) #Replace /path/to/dir with a path to a dir.
    print(files)

The above code uses a very basic regex pattern to find files recursively that either contain the keyword 'food' or 'foot'. 

.. note::

    If you use the exactSearch parameter by setting it to True, make sure to include the file extension (unless, of course, the file has no extension)


``scanFilesForContent``
-----------------------

The ``scanFilesForContent`` function is used in order to scan file content for a specific keyword. If a file contains that specific keyword, the file and its path is appended to a list, which is later on returned.

It takes in two required parameters: contentKeyWord (str), dir path. (str)

It takes in three optional parameters: fileExtension (list), recursive (boolean), regex (boolean)

The contentKeyWord is the keyword to search for within the file. The dir path is the path to scan the files and their content for that keyword. 

The fileExtension parameter can be used in order to only scan files with specific file extensions. It is in the form of a list as you can add as many filters as you want.

The regex option is there in case you want to use regex, similarly to the findFiles function.

In order to use the function, you can do so like this:


.. code-block:: python

    files = fileOperands.scanFilesForContent('keyword', '/path/to/dir', extensionFilters = ['.py', '.sh'], recursive = True) #Replace keyword with a key word, /path/to/dir with a path to a dir.
    print(files)

The above code finds a keyword recursively through the given path, but only scans through .py and .sh files, as those are the ones specified uner extensionFilters. 

.. note::

    If the extensionFilters parameter is left empty, all files (which can be decoded) will be scanned. 

``removeFiles``
---------------

The ``removeFiles``  function is used in order to guide you into removing files. It does require user interaction, as this may be dangerous.

It takes in two required parameters: fileName (str), dir path (str)

It takes in four optional parameters: exactSearch (boolean), extensionFilters (list), recursive (boolean), regex (boolean)

The above options are much like the scanFilesForContent and findFiles functions.

You can run the function like so:

.. code-block:: python

    fileOperands.removeFiles('keyword', '/path/to/dir', extensionFilters = ['.py'], recursive = True) #Replace keyword with a key word, /path/to/dir with a path to a dir.

The above code recursively finds and (with user confirmation) removes the files with the specified keyword, and, as seen in the previous functions, will follow the extensions filter if there are any filters included. Regex may be used, as well as exactSearch.

The user confirmation will look something like this:::

    File Found at:
    /path/to/file

    You are about to delete this file. Continue? ((1) Yes / (2) No): 

The user will be prompted to continue with the removal of the file. For each file with the matching key word, there will be a prompt to ask whether or not to remove it.

``createFiles``
---------------

The ``createFiles`` function is a function used to create how ever many files as specified in a certain path. It adds a number after the file name, which is inputted by the user, for each file created. 

It takes in four required parameters: createAmount (int), keyWord (str), extensionType (str), dir path (str).

It takes in one optional parameter: fileStartsAtOne (boolean)

If you want to create 3 files in a directory, and the keyword for the file names is "FILE", the files will be created like so: FILE, FILE2, FILE3.

If you use the firstFileStartsAtOne parameter, the first file will contain the number 1. So, instead of just FILE, it would be FILE1.

You can use the function like so:

.. code-block:: python

    fileOperands.createFiles(5, 'FILE', ".py", "/path/to/dir", firstFileStartsAtOne = False) #Replace int '5' with whatever number you want, FILE with your own key word, /path/to/dir with a path to a dir.

The above code creates 5 files, with a .py extension, in the specified path. The firstFileStartsAtOne boolean is set to False, so the first file does not contain a number after the given keyword.

``findAndReplaceInFiles``
-------------------------

The ``findAndReplaceInFiles`` is not your usual find and replace that you use in a file. Instead, it is a global find and replace. It is used to scan through (decodable) files, and replace a key word with a replacement key word throughout each file containing the key word.

.. note::

    If not used with caution, the ``findAndReplaceInFiles`` can cause damage. As stated before, I am not responsible for any data loss done by the library. 


It takes in three required parameters: keyWord (str), replacementKeyword (str), dir path (str)

It takes in one optional parameter: recursive (boolean)

You can execute the function like so:

.. code-block:: python

    fileOperands.findAndReplaceInFiles('This is the old word', "This is the new word", "/path/to/dir", recursive = True) #Replace the keyWord and replacementKeyword parameters with strings of your own. /path/to/dir with a path to a dir.

In the above code, 'This is the old word', is the string, or key word, that the function searches for, and 'This is the new word', is the replacement key word that replaces 'This is the old word'. The recursive option is set to True, and this will make the function scan recursively through the given path and search every (decodable) file for the key word to replace.

``insertTextInFile``
--------------------

The ``insertTextInFile`` function can be used in order to insert text in a specific line of a file.

It takes in three required parameters: insertionText (str), lineNumber (int), file path (str)

It takes in one optional parameter: appendNewLines (boolean)

The insertionText parameter is the text to insert at the lineNumber parameter given within the file under the file path parameter.

The appendNewLines is a special option that allows the user to bypass the restriction of only writing to lines within the files' line amount. For example, if a file has 10 lines, and the user wants to write to line 15, the appendNewLines parameter will make this possible.

In order to use this function, you can do so like this:

.. code-block:: python

    fileOperands.insertTextInFile('This text is inserted in line 5', 5, "/path/to/file", appendNewLines = False) #Replace the parameters with values of your own. /path/to/file with a path to a file.

The above code will write 'This text is inserted in line 5' in line 5 of a given (decodable) file. The appendNewLines parameter is set to False, as, the file as an example already had at least 5 lines.

.. note::

    The next several functions are very basic file operations. Because of this, the explanations will be much shorter.

``moveFile``
------------

This function takes in two required parameters, the first being the original file path (the one to move), and the second being the directory of where to move it to.

You can use it by calling the function like so:

.. code-block:: python

    fileOperands.moveFile("/path/to/file/to/move", "/path/to/dir/to/move/file/to") #Replace the two paths with valid paths (The first with a path to a file, second to a path of a directory)

``copyFile``
------------

This function is very similar to the ``moveFile`` function, and takes in the same parameters. Instead of moving the file, however, it copies it.

``moveDir``
-----------

This function moves a directory and all of its contents to another directory, and takes in two required parameters: The first being the one to the directory to move, and the second being the directory to move the directory to.

``copyDir``
-----------

This function takes in the same parameters as the ``moveDir`` function, but copies the directory instead of moving it.

``renameFile``
--------------

This function takes in two required parameters: The first being the new name for the file (This includes the file extension!), and the second being the file path, which is the path to the file to rename.

``renameDirectory``
-------------------

This function is very similar to the ``renameFile`` function, but it renames a directory instead. You can use it similarly to the ``renameFile`` function, but instead of a path to a file to rename, it is a directory.

``createFile``
--------------

This function takes is two required parameters, the first being the name of the file to create (which includes the extension), and the path where to create the file.

``removeFile``
--------------

This function only takes in one required parameter, which is the path to the file to remove.

.. note::

    The **Logging** class will not be covered here, as the user does not have any use of any functions in this class. The Logging class is solely used by the program in the **Synchronize** and **Backup** classes, covered below.

.. _synchronize function use:

**Synchronize** Usage
=====================

.. note::

    The **Synchronize** class really only has one function that the user uses in order to use the synchronization properly. Although it is only one function, it is very complex (not to use, but rather how it works). Because of this, only the ``synchronize`` function will be explained here.

``synchronize``
---------------

**IMPORTANT NOTE**
.. note::

    Before using these functions, do keep in mind: It is highly dangerous to rename a directory or file as the last thing to do if you did other actions before (such as add files/dirs). This could lead to data loss! You should synchronize every time you add, remove, etc. something. 

The ``synchronize`` function is a very complex function that the user can however use with ease. The main purpose of this function is to take in two directories, and synchronize them and their files.

First, lets take a look at the features:

* Synchronization of files and directories (gets the time last modified of both. The one last modified gets the synchronization priority.) This includes, copying, removing, renaming, etc. to files/dirs.
* Automatic renaming and updating of file content based on last modification times.
* Automatic merging recognition. (This is done by hash computation. If no hashes match in each of the same directories within the two directories to synchronize, then merge (as no files are matching). If there are matching hashes, do something like remove a file instead of merging it).
* Includes an importantFilesFlag (A custom importantFilesFlag is also possible, but it defaults to an underscore '_'). This is a character that goes at the beginning of a file or dir. These important files/dirs are flagged by the Synchronization class, and if one is deleted, it will be restored no matter what. On other words, they are impossible to be deleted by the library itself. In order to delete important files/dirs, they must be deleted on both directories.
* Optional backup folder. This is useful if you want to make sure no data is lost by accident. It will automatically move everything deleted in this folder.
* Optional, complete and detailed logging, which can be saved to a file to a custom path for complete analysis of each process.

The **Synchronization** class is filled with features that are super useful to synchronize two directories effectively. Now, lets go over the usage of these functions.

The ``synchronize`` function takes in two required parameters. That's it! These are: dir1 (str), dir2 (str)

It also takes in four optional parameters: importantFilesFlag (str), syncBackUpFolderExists (boolean), loggingBool (boolean), logCreationPath (str).

If you want to most basic usage, you can execute it like so:

.. code-block:: python

    Synchronize.synchronize("/path/to/dir1", "/path/to/dir2")

The above code has all options set to default. This means: importantFilesFlag = '_', or an underscore, syncBackUpFolderExists = True, a sync backup folder will be created in case of accidental file removals. And, for the logging, it is disabled.

The importantFilesFlag is a character that you as the user can use to mark certain files as important. This is explained under the features right above.

For example, if the importantFilesFlag is left to a default (which is an underscore), an important file would look like this:::

    _importantFile.txt

**IMPORTANT NOTE**
.. note::

    Concerning the sync backup folder, it is totally recommended that you use it. PLEASE NOTE: IF YOU RUN THE SYNCHRONIZATION FOR THE FIRST TIME, RUN THE FIRST TIME WITH THE SYNCBACKUPFOLDER SET TO TRUE. This is to prevent initial data loss! As stated before, I am not responsible for any data lost. Initially, to learn how this works, use the backup folder to prevent data loss! You an disable it by putting the parameter to False, if you really need to.

    PLEASE KEEP IN MIND: If you have dir1 and dir2, and you have a folder in dir1 but dir2 is empty (or viceversa), and then, renaming dir2 is the last thing you do, you could risk data loss, as the function will think you want to delete the folder from dir1 (because dir2 was the last one modified)


The sync backup folder will always be marked with the important files flag so that it isn't accidentally removed. If the importantFilesFlag is left to its default value of an underscore, the sync backup folder would look like this:::

    _syncBackups

.. note::

    Please do note that the syncBackups folder will always be stored within the root directory of the given paths for dir1 and dir2. 

Now, for the logging. The logging is very easy to use. It provides very detailed information about which actions are performed, when they are performed, and even which mode (Synchronize or Backup) were used. (Backup is explained later on).

If you want to use logging, all you need to do is set the loggingBool to True, and put a path to a directory where to create the log files.

.. code-block:: python

    Synchronize.synchronize("/path/to/dir1", "/path/to/dir2", loggingBool = True, logCreationPath = '/path/to/logcreationdir')

A log will have log tags, which are either NC (Non critical) or C (Critical). This is used in order to easily find the more important activites (C), such as removing or adding files.

A log will also have the time at which each process happened. It may seem like the time never changes, but this is solely due to the fact that the function executes very fast (so it will usually remain within the same second by the time the whole process ends)

**Backup** Usage
================

The **Backup** class is very similar to the **Synchronize** class, but it uses a main directory as its bias as to what to follow.

For example, if you have a main directory, such as maindir , it will backup to a directory, for example, backupdir. Anything done to the backupdir will be ignored, while everything in the maindir will be done in the backupdir. For example, if you try to add a file in the backupdir that isn't in the maindir, it will be removed. If you try to remove a file in the backupdir, it will be added again (because the maindir contains the file and the backupdir does not).

The **Backup** class contains two main functions that you as the user can use: ``backup``, and ``backgroundBackup``.

Both of these functions, unlike the ``synchronize`` function in the **Synchronize** class, support and as many backup directories as you want. If you want to backup to three directories, you can. 10, 20, 1000 directories, you can!

``backup``
----------
 The ``backup`` function is the main function of the class.

 It takes in two required parameters: maindir (str), backupdirs (list)

 It takes in two optional parameters: loggingBool (str), logCreationPath (list).

 In order to use it, you can do so like this:

.. code-block:: python

    Backup.backup("/path/to/maindir", ["/path/to/backupdir1", "/path/to/backupdir2"], loggingBool = True, logCreationPath = '/path/to/logcreationdir')

The above code backs up everything in maindir to backupdir1 and backupdir2. Of course, you can have more than two backup dirs, but there are two just as an example. Here, logging is enabled, so that will work. 

``backgroundBackup``
--------------------

The ``backgroundBackup`` function is basically the same thing as ``backup``, but it actually goes in the background. It has an extra optional (default = 8) refreshInterval parameter, which defines the interval (in seconds) for each backup.

You can leave this in the background running and it will backup every time the refreshInterval strikes again.


.. note::

    It is reccomended that you use logs in order to prevent data loss. Logs help you (and me) figure out what went wrong or what you can do to retreive the file back/ what happened during a specific process.


**callBash** Usage
==================

``runFile``
-----------

This function can simply be used to run a shell script. It takes in one required parameter, the path to the shell script, and has an optional parameter to edit the permissions of the file to avoid executable issues.