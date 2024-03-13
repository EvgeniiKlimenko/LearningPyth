# basic implementation of decorator:
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"=> Before call the func")
        result = func(*args, **kwargs)  # to return some result
        print(f"=> After call the func")
        return result  # to return some result

    return wrapper


@my_decorator   # put the decorator above the function we want to decorate
def say_hello(*, name: str) -> str:
    print("Constructing the greeting...")
    hello = f"Hello {name}"
    return hello


# without a decorator:
# my_decorator(say_hello())()

# with decorator:
greeting = say_hello(name="Ms. Smith")
print(greeting)
