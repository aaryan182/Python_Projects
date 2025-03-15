# Python decorators modify function behavior like middleware in js

def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with arguments {args}")
        return func(*args, **kwargs) # calls the original function
    return wrapper

@log_function
def add(a, b):
    return a+b

print(add(5,10))