def star_decorator(func):
    def wrapper():
        result = func()
        return "*****" + result + "*****"
    return wrapper


@star_decorator  
def say_hello():          
    return "Hello"

print(say_hello())