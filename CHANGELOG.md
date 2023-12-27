## FinderZ Changelog (From V 2.1.2 Onward)

**CHANGELOG Start Date:** December 27, 2023
**LATEST VERSION:** 2.1.2 (December 27, 2023)


# **FinderZ Release 2.1.2 (December 27, 2023)**

FinderZ Release 2.1.2 includes a variety of new functions:

**GatherInfo Class:**
1. isHiddenFile(file_path) —> This function returns either True or False, whether or not the file specified in the path file_path starts with a ‘.’
2. getAllHiddenFIlesInDir(dir) —> This function takes in the path of a directory and scans the files within that directory. It returns a list of all the hidden files’ paths in the directory.
3. getAmountOfEachFileTypeInDir(dir, recursive = False) —> This function takes a path to a directory (and an option to scan that directory recursively). It returns a dictionary which contains each file extension type as the key, and the amount of that file extension type as the value. So, the returned dictionary, as an example, could look something like this: {'.py': 80, '.txt': 7}. In other words, in the directory, there were a total of 80 .py files and 7 txt files (note that the amounts are in order).

**fileOperands Class:**
4. removeAllFilesInDir(dir, removeDirectories = False) —> This function takes in a directory and removes all the files in a directory, as well as an optional parameter that can be enabled to delete directories and their contents as well. It does NOT have a recursive option, but rather just a single ‘wipe out’ method of deleting files quickly.


The new functions in the fileOperands class also include the addition of XOR encryption/decryption of files as well as directories:


2. xor_encrypt_file(file_path, key, removeOriginal = False) —> This function encrypts a specific file with a specific key, and even has an optional parameter removeOriginal, which essentially decides whether or not to remove the original file after the encrypted file is created. For example, say you have text.txt as a file in a directory. You put the path of this file into this function, and choose a key. If removeOriginal is false, the text.txt will remain. However, if it is true, the text.txt will be deleted, and the only thing that will remain will be text.txt.enc, which is the encrypted file. Please note, that the encrypted files will end up with the extension ‘.enc’.
3. xor_decrypt_file(enc_file_path, key, removeEncrypted = False) —> This function does pretty much the same thing as the encryption function, but rather in reverse. However, instead of removeOriginal, it has removeEncrypted, which means that as soon as the given encrypted file is decrypted, it decides whether or not to keep the encrypted file or not once it is decrypted. Please make sure to have the same key when encrypting and decrypting.
4. xor_encrypt_files(dir, key, removeOriginal = False, recursive = False) —> This, unlike the encryption of just one file, rather takes in a directory as a parameter and has the option of encrypting all files with a specific key in a directory recursively as well. It takes in a directory path, and encrypts all the files within the directory with a specified key.
5. xor_decrypt_files(dir, key, removeEncrypted = False, recursive = False) —> Again, very similar to the xor_encrypt_files function, but rather it does the opposite. Make sure again to have the same key as when you encrypted the files you are trying to decrypt.
6. removeEncFiles(dir, recursive = False) —> This function is just a way for you to remove a left over .enc files in a directory. You can make it do so recursively as well.

Please be patient, as documentation will be updated soon. As far as the Synchronize class, plans are being made to enhance usability. 

Also, the code for certain functions will be optimized/made shorter, as I have found certain ways to make certain functions much more compact. In the next update (2.1.5) , the documentation will be updated to release 2.1.5, and the library size will be decreased (estimated to around 30-40% less).

Thank you for 28K downloads!
