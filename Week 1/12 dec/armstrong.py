# ---Armstrong Number---
#This is a number whose sum of cube of individual digit is equal to the number itself
#Ex- 371 -> 3^3 + 7^3 + 1^3 => 27 + 343 + 1 => 371

number = int(input("Enter a Number: ")) 
original_number = number
sum_of_cubes = 0

while(number!=0):
    digit = number % 10
    sum_of_cubes = sum_of_cubes + (digit**3)
    number = number // 10

if(original_number == sum_of_cubes):
    print("Number is an Armstrong")
else:
    print("Number is not an Armstrong")