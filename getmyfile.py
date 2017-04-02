"""
@author: Oladimeji Salau

Purpose: A python code to search computer for a given file name and returns the file location.

How to use it
==============
Call the function with the name of the file to be searched as an argument and run the code.

Requirements
============
None

"""

import os

def getmyfile(named):
    '''this function searches the system for a given filename'''
    try:
        result = []
        rootDir = os.getcwd()[0]

        for dirName, subdirList, fileList in os.walk(rootDir):
            for fname in fileList:
                remove_ext = os.path.splitext(fname)[0]
                filename_str = remove_ext.split('/')[-1]

                if filename_str.upper() == named.upper():
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
                "ehm...sorry. I've searched really well. I don't seem to have a file with this name."
            )

    except Exception as err:
        print(err)
