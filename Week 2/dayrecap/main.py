#This file is for inputing and printing the results.

from file import find_files               #Import find_files function

path = input("Enter directory path: ")    #takes input from user

python_files_list, other_files_list = find_files(path)    #calls the function from find_files

print("--- Found these Python Files ---")
print(python_files_list)

print("--- Found these Other Files ---")
print(other_files_list)