def decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper


@decorator
def say_hello():
    print("Hello, world!")


say_hello()
