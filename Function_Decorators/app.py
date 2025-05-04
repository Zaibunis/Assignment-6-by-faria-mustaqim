def log_function_call(func):         # Decorator function
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

@log_function_call                   # Apply the decorator
def say_hello():
    print("Hello!")

say_hello()
