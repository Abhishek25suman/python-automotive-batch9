def add(a, b):
    return a + b

def calculator(func):
    def wrapper(p, r, t):
        return add(p, (p * r * t) / 100)
    return wrapper

@calculator
def simple_interest(p, r, t):
    pass

p = float(input("Enter p: "))
r = float(input("Enter r: "))
t = float(input("Enter t: "))

print("Total Amount:", simple_interest(p, r, t))