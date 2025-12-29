students = {}

def school_manager(choice):
    def decorator(func):
        def inner():
            if choice == 1:
                student_id, name, cls, marks = func()
                students[student_id] = {
                    "name": name,
                    "class": cls,
                    "marks": marks
                }
                print("Student added successfully.")

            elif choice == 2:
                student_id, subject, marks = func()
                if student_id in students:
                    students[student_id]["marks"][subject] = marks
                    print("Marks updated successfully.")
                else:
                    print("Student not found.")

            elif choice == 3:
                if not students:
                    print("No student records available.")
                else:
                    for sid, details in students.items():
                        print(f"\nID: {sid}")
                        print(f"Name: {details['name']}")
                        print(f"Class: {details['class']}")
                        print("Marks:")
                        for sub, m in details["marks"].items():
                            print(f"  {sub}: {m}")
            else:
                print("Invalid choice.")
        return inner
    return decorator


print("1. Add Student")
print("2. Update Marks")
print("3. Display Students")
choice = int(input("Enter your choice: "))


@school_manager(choice)
def manage():
    if choice == 1:
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        cls = input("Enter Class: ")
        n = int(input("Enter number of subjects: "))
        marks = {}
        for _ in range(n):
            subject, score = input("Enter subject and marks: ").split()
            marks[subject] = int(score)
        return student_id, name, cls, marks

    elif choice == 2:
        student_id = input("Enter Student ID: ")
        subject = input("Enter Subject: ")
        marks = int(input("Enter Marks: "))
        return student_id, subject, marks


manage()