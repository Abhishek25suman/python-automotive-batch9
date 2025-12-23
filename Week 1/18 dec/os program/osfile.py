import os   #built-in package of os module

def show(path):    #show() is user defined function
    files = []     #stores files
    folders = []   #stores folders

    for name in os.listdir(path):
        if os.path.isfile(path + "/" + name):  #isfile() is builtin function in os module
            files.append(name)
        else:
            folders.append(name)

    return files, folders
