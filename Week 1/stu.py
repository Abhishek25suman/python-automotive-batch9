students_list = [
    "Abhishek Suman", "Amit Verma", "Sneha Patel", "Rahul Singh", 
    "Priya Das", "Vikram Rao", "Amit Kumar", "Rohan Gupta", 
    "Sristy Singh", "Kavita Mishra", "Arjun Reddy", "Pooja Mehta", 
    "Vikas Jain", "Anjali Gupta", "Rohini Joshi", "Neha Kapoor", 
    "Suresh Kumar", "Puja Bhatt", "Karan Malhotra", "Vikash ravi"
]

duplicate_list = []
duplicate_dict = {}

for i in range(len(students_list)):  
    fullname1 = students_list[i].split()
    name1 = fullname1[0]
    surname1 = fullname1[1]
    

    for j in range(i + 1, len(students_list)):  
        fullname2 = students_list[j].split()
        name2 = fullname2[0]
        surname2 = fullname2[1]

        if name1 == name2 and surname1 != surname2:
            duplicate_dict = {
                "Student 1": f"{name1} {surname1}",
                "Student 2": f"{name2} {surname2}"
            }
            
            duplicate_list.append(f"Duplicate Names are {name1} {surname1} and {name2} {surname2}.")

            print(f"Result from List: {duplicate_list[0]}")
            print(f"Result from Dictionary: {duplicate_dict}")
            
            exit() 

else:
    print("No duplicates found in the entire class.")