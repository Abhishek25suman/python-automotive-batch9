try:
    num = int(input("enter a number: "))
    result = 10 / num
    print("result is:", result)

except ZeroDivisionError:
    print("the divisor cannot be 0")

except ValueError:
    print("the divisor is non numeric")

finally:
    print("everything done")
