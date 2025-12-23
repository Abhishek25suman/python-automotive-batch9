#tuple collection which is ordered and unchangeable, used to group together related data.

car = ("BMW", 2025, "Black")
print(car.count("BMW"))
print(car.index("Black"))
for i in car:
    print(i)
if "BMW" in car:
    print("BMW is here!")