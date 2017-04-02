"""
Created on Wed Mar 15 2017
@author: Oladimeji Salau

Purpose: A python code to properly counts files in a given directory and returns the result.

How to use it
==============
Call the function with a directory path containing files to be counted as an argument and run the code.

Requirements
============
None

"""

import os 

def countfile(dir_path):
    '''this function counts files in a given directory and returns the result'''
    try:
        flist = []
        for d, s, f in os.walk(dir_path):
            flist.extend(f)  
    except exception as err:
        print(err)
    
    return len(flist)
