print("Get max, min swap value of variables")
print("\n 1.Max \n 2.Min \n 3.Swap")

a, b = map(int, input("Enter two numbers: ").split(","))
choice = int(input("Enter your Choice: "))

if choice == 1:
    print(f"The Maximum is: {max(a, b)}")
elif choice == 2:
    print(f"The Minimum is: {min(a, b)}")
elif choice == 3:
    a, b = b, a
    print("After swapping: a = %d, b = %d" % (a, b))
else:
    print("Invalid Choice")