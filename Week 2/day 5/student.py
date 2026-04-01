# ---Finding Duplicate Students Name---

# write a python program that will have usecase of school having 20 students 
# and we have to find out that student whose name is the same with another student 
# but surname is different. Maintain only one duplicate

students_list = [
    "Abhishek Suman", "Amit Verma", "Sneha Patel", "Rahul Singh", 
    "Priya Das", "Vikram Rao", "Amit Kumar", "Rohan Gupta", 
    "Sristy Singh", "Kavita Mishra", "Arjun Reddy", "Pooja Mehta", 
    "Vikas Jain", "Anjali Gupta", "Rohini Joshi", "Neha Kapoor", 
    "Suresh Kumar", "Puja Bhatt", "Karan Malhotra", "Vikash ravi"
]

# Check 20 students
for i in range(len(students_list)):  
    fullname1 = students_list[i].split()
    name1 = fullname1[0]
    surname1 = fullname1[1]
    # Extract and splits the name of the 1st student as name1 and surname1

    # Compare with remaining students
    for j in range(i + 1, len(students_list)):  
        fullname2 = students_list[j].split()
        name2 = fullname2[0]
        surname2 = fullname2[1]
        # Extract and splits the name of the next student in the list as name2 and surname2

        #Checking first name matches or not and surnames are different
        if name1 == name2 and surname1 != surname2:
            print(f"Duplicate Names are {name1} {surname1} and {name2} {surname2}.")
            exit() 
            # Program Stops 