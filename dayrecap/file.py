#This file is for dividing the different types of file in directory path. 

import os

def find_files(path):
    python_files = []   # List for .py files
    other_files = []    # List for everything else
    
    all_items = os.listdir(path)       #extract all the files from that path
    
    for name in all_items:
        if name.endswith(".py"):        #checks for .py files
            python_files.append(name)   #adds python files
        else:
            other_files.append(name)    #adds other files
            
    return python_files, other_files