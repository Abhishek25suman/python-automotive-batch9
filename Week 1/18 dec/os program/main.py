from osfile import show      #import show 
from input import take_path

path = take_path()               # get directory path
files, folders = show(path)      # call function

print("Files:", files)
print("Folders:", folders)
