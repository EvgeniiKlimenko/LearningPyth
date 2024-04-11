# Basic class for exceptions - BaseException.
# For instance: BaseException -> Exception -> ArithmeticError -> ZeroDivisionError


class MyCustomException(Exception):
    def __init__(self, *args):  # here will be a message from 'raise MyCustomException(...message...)'
        self.message = args[0] if args else None  # if args is empty - then self.message = None

    def __str__(self):
        return f'Error: {self.message}'


try:
    x, y = map(int, input("Enter the values: ").split())
except (ValueError, FileExistsError) as err:  # several exception types in one except block
    print("Value error!")
    print(f"Exception instance: {err}")
except ZeroDivisionError:
    print("Cant divide by zero")
else:
    print("No exceptions have happened.")
finally:
    print("Is executed always, in any cases")

# finally - is executed before return, in case it exists in function, and we have return in except: block
# use except: without specifying the type of exception - will catch ANY exceptions
# try:
# with open("file.txt") as file: ... -> try with resources

raise MyCustomException("Custom exception was generated! Great job!")


