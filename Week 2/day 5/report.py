# ---Report Card Program---
#this program checks the marks of the student and provides the report card with final status as pass or fail.

def calculate_total(marks_list):
    return sum(marks_list)  # Built-in function sum() inside def

print(" ---Report Card---")
name = input("Enter Name: ")
s1 = int(input("Subject 1: "))
s2 = int(input("Subject 2: "))
s3 = int(input("Subject 3: "))

#storing marks in a list
marks = [s1, s2, s3]

#calling the function where sum of marks is stored
total_marks = calculate_total(marks)
average = total_marks / 3

print("Name: ", name)
print("Total Marks: ", total_marks)
print("Average: ", average)

if average >= 60:
    print("Result: PASS")
else:
    print("Result: FAIL")