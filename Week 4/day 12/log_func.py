def log_function(func):
    def wrapper(*args, **args2):
        print("calling function:,{func.__name__}")
        result =func(*args, **args2)
        print("function executed:,{func.__name__}")
        return result
    return wrapper


@log_function
def greetin(name):
 return (f"hello,{name}")