# -*- coding: utf-8 -*-
"""
@author: Oladimeji Salau

Purpose: A python code containing useful functions for managing files and directories.

How to use it
==============
Save the code as dfmtool.py and run it on your system's terminal.

Requirements
============
Ensure relevant python modules as noted below are installed on your system.

"""

# import relevant modules
import os, sys
import time
import shutil
import re
from sys import platform as myplatform

# Check Platform
if myplatform == "linux" or myplatform == "linux2":
    clear_screen = os.system('clear')
elif myplatform == "darwin": # mac
    clear_screen = os.system('clear')
elif myplatform == "win32": # windows
     clear_screen = os.system('cls')

# Menu function
def menu():
    clear_screen
    print('''
    ====================================================================
     Name:    Directory & File Management Tool (DFMTool)
     Author:  Oladimeji Salau
    ====================================================================
    1. Count folders and files in a given directory
    2. Search for a given file name in a certain directory
    3. Search files in a directory using extension type
    4. Backup files to a target directory
    5. Exit
    ====================================================================''')
    print()
    choice = str(input("Enter a choice and press enter: " ))
    print()
    return choice

#*************************************************************************

# Folders and Files Count function
def DirFileCount(mydir):
    '''this function counts files and folders in a given directory and returns the result'''
    if os.path.exists(mydir): # check if path provided exists
        try:
            # create lists to hold files and folders
            flist = []
            dirlist = []
            
            # searching the directory provided
            for d, s, f in os.walk(mydir):
                flist.extend(f) 
                dirlist.extend(s)    
        except exception as err:
            print(err)   
        
        print('Total number of files in '+ os.path.join(d, mydir)+' is: {}'.format(len(flist))) 
        print('Total number of folders in '+ os.path.join(d, mydir)+' is: {}'.format(len(dirlist)))
    
    else:
        print("Sorry, the directory entered does not exist!")


    
#File Search by name function
def FileSearchByKeyword():                 
    for dirpath, dirs, files in os.walk(mydir):
        for mfile in files:
            path = os.path.join(dirpath, mfile)
            path = os.path.normpath(path)
            if re.match("(.*)%s(.*)"%res, mfile, re.IGNORECASE):
                print(path)
    
         
def GetMyFile():
    '''this function searches the system for a given filename'''
    try:
        result = []
        rootDir = os.getcwd()[0]

        for dirName, subdirList, fileList in os.walk(mydir):
            for fname in fileList:
                remove_ext = os.path.splitext(fname)[0]
                filename_str = remove_ext.split('/')[-1]

                if filename_str.upper() == res.upper():
                    fnamepath = os.path.join(dirName, fname)
                    result.append(fnamepath)
                else:
                    pass

        if result:
            print(
                "File or files with similar names in this computer are listed below: "
            )
            for i, k in enumerate(result, start=1):
                print(i, k)
                  
        else:
            print(
                "There is no file with exact name in this directory."
            )
            
            option = input('Do you want to search for files that have names like the one you are searching for in this folder? Note: result may be many. (Yes or No):')
            if option.upper() =='YES':
                print()
                FileSearchByKeyword()
            if option.upper() =='NO':
                print()
                print('OK. Bye')
                pass
                  
    except Exception as err:
        print(err)
              
              
# File extension function
def FileExt(mydir):
    if os.path.exists(mydir):
        for dirpath, dirs, files in os.walk(mydir):
             for mfile in files:
                mpath = os.path.join(dirpath, mfile)
                mpath = os.path.normpath(mpath)
                if mfile.endswith(ext):
                    print(mpath)                 
    else:
        print("Sorry, the directory entered does not exist!")

                           
# File backup function
def Zipbacky():
    # get source directory of files to be backed up as input from user
    sourcedir = input('Enter here the source directory of files to be backed up: ')

    # derive the target directory
    mydt = time.strftime('%d%B%Y')
    myt = time.strftime('%H%M%S%p')

    targetdir = sourcedir + '_' + 'Backup' + '_' + mydt + '_' + myt

    # zip the source directory
    file_archive = shutil.make_archive(targetdir, 'zip', sourcedir)

    # confirm if user want to move the final zipped folder into a new location
    if file_archive:
        location = input('Do you want to put the backup in a different directory? (Yes or No): ')
        if location.upper() =='YES':
            newlocation = input('Specify new location to keep the backup: ')
            shutil.move(file_archive, newlocation)
            print('Successful backup to:', newlocation)
        if location.upper() =='NO':
            print('Backup SUCCESSFUL!')
    else:
        print('Backup FAILED!')

#**********************************************************************

# Decision Menu
choice = menu()
if choice == "1":
    clear_screen
    print()
    mydir = str(input('Enter path of directory in which files and folders will be counted: '))
    DirFileCount(mydir)


if choice == "2":
    clear_screen
    print()
    mydir = str(input('Enter path of directory to search: '))
    if os.path.exists(mydir):
        res= str(input('Enter the file name you want to search: '))
        GetMyFile()
    else:
        print('The directory provided does not exist')
        

if choice == "3":
    clear_screen
    dirpath = str(input("Enter the path of the directory to be searched: "))
    print()
    ext = str(input("Enter desired file extension, (e.g. pdf): " ))
    print()
    print('''
    The desired file type: %s are listed as follows:
    ==================================================
    ''' % (ext))
    FileExt(dirpath)

if choice == "4":
    clear_screen
    Zipbacky()


if choice == "5":
    clear_screen
    quit()