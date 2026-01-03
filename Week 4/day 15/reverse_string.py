# Decorator definition
def reverse_decorator(func):
    def wrapper(self, text):
        result = ""
        for char in text:
            result = char + result   # manual reverse logic
        return func(self, result)
    return wrapper


# Class definition
class StringReverse:

    @reverse_decorator
    def show_result(self, reversed_text):
        return reversed_text


# User input
user_input = input("Enter a string: ")

# Object creation
reverse = StringReverse()

# Output
print("Reversed string:", reverse.show_result(user_input))