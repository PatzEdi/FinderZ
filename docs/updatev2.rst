.. _updatev2:

*******************
FinderZ V2 is Out!
*******************

.. note::

   FinderZ V2 introduces many new and useful features to the FinderZ library. This part of the documentation explains these new features. Some of these new features are actual classes, but those will not be talked about here, and will rather be referenced in the :doc:`function use` section of this guide.

What's new in V2: Complete Changelog:
=====================================

FinderZ V2 introduces many new things:

Major Changes:
--------------

* Introduction of the documentation you are reading now.
* Added Synchronization and Backup of directories. More info on that under the :doc:`function use` section of the documentation.
* Added Regex options to some functions in order to search for specific things.
* Added a recursive option to some functions. Now, you can also perform actions on single directories, instead of defaulting to recursiveness.
* Added many new functions to the GatherInfo class. More on that below on :ref:`gather info v2 funcs`.
* Completely redid some functions in order to improve reliability and efficiency.
* Removed the ``findFile`` function due to the implementation of an exactSearch parametric boolean. With this new parameter, you can choose whether or not to find for a keyword within something or a keyword that exactly matches something.

Minor Changes:
--------------

* Made the parametric 'fileExtension' variable optional under the scanFilesForContent function (Now, by default, all files are include no matter the extension type. But you can specify it if needed!).
* Many big and minor fixes. Lots of unnecessary code removed.
* Improved function reliability by replacing some forms of dealing with directories with more reliable ones.

.. _gather info v2 funcs:

GatherInfo V2 Functions
=======================

These are the new functions that are now inlcuded in the **GatherInfo (GI)** class:

* isEmptyDir() - Check whether or not a directory is empty (return = type bool)
* computeHash() - Hash computation. Now, hashes can be computed on files. (return = type str)
* isOneInCommon() - Check whether or not two lists have at least one element in common. Mostly intended to be used by the library, not much use for the user. (return = type bool)
* readDir() - One of the more important new functions under the **GI** class. Used to return directories or files in a directory, or even both. (return = type list)
* isRegexAndStringMatching() - Mostly intended to be used by the library, but can be used by the user as well. This function can determine whether or not a pattern is present or even exactly matching a string. (return = type bool)
* getTotalInfo() - Gathers the total amount of lines and optionally even files within a directory. Either recursive or not, includes a extensionFilters parameter which takes in a list for counting files only with specific extensions.


Update V2 is a huge update for FinderZ. It includes a plethora of features which make FinderZ a more usable, efficient, and better file operation tool for Python in general. 