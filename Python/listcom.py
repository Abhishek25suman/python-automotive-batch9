# this program creates a new list replacing scores below 70 with 'Failed'.

students = [100, 90, 80, 70, 60, 50, 40, 30,0]

pass_students = [i if i >= 70 else "Failed" for i in students]
print(pass_students)