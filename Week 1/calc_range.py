def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b

operations = [add, sub, mul, div]

print("1.Add 2.Subtract 3.Multiply 4.Divide")
choice = int(input("Enter choice: "))

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

for i in range(len(operations)):
    if choice == i + 1:
        result = operations[i](x, y)
        print("Result:", result)
        break
else:
    print("Invalid choice!")