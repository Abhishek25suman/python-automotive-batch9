def calculator(choice):
    def calculator(func):
        def inner():
            a, b = func()
            if choice == 1:
                return a + b
            elif choice == 2:
                return a - b
            elif choice == 3:
                if b == 0:
                    return "Cannot divide by zero"
                return a / b
            else:
                return "Invalid choice"
        return inner
    return calculator

print("Enter two numbers:")
x, y = map(int, input().split())

print("Enter your choice:")
print("1. Addition")
print("2. Subtraction")
print("3. Division")
choice = int(input())

@calculator(choice)
def calculate():
    return x, y

print("Result:", calculate())