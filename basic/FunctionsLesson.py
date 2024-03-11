
test_numbers_1 = [1, 4, 6, 8, 12, 6, 7]
test_numbers_2 = [7, 14, 16, 18, 12, 8, 24]


def count_average(number_list):
    result = sum(number_list) / len(number_list)
    return result


average_result_1 = count_average(test_numbers_1)
print(average_result_1)
average_result_2 = count_average(test_numbers_2)
print(average_result_2)


def count_vowels(string):
    VOWELS = "aeiouyAEIOUY"
    count = 0
    for char in string:
        if char in VOWELS:
            count += 1
    return count


print(count_vowels("Hello, world of Python"))


# empty function example
def empty_func():
    pass


# declare type of parameters and
# return value type(optional, not fail anything, just to readability)
def format_date(day: int, month: str) -> str:
    return f"The day is {day}, and month is {month}"


print(format_date(day=25, month="December"))  # to avoid confusion, if no types are declared


def force_par_names(*, number, string):  # in this case we CAN'T call ...(44, "Python")
    return f"Force user to use named parameter: {number}, and  {string}"


print(force_par_names(number=44, string="Python"))


# default values for the parameters
def default_values_example(*, minutes: int = 1, hours: int = 1, days) -> str:
    return f"Minutes: {minutes} and hours: {hours} with days: {days}"


print(default_values_example(days=2))  # now, we can call it only with days


def add_all(*args):  # var args function
    type(args)  # type is tuple
    summary = 0
    for num in args:
        summary += num

    return summary


print(add_all(1, 2, 3, 4, 9))
numbersList = [5, 12, 1, 165, 87, 86, 11]
other_numbers_list = [52, 12, 1, 16, 87, 8, 11]
print(add_all(*numbersList, *other_numbers_list))  # use asterisk to pass different lists


def kwargs_function(**kwargs):  # accepts any number of key=value pairs
    type(kwargs)  # type is dictionary
    print(kwargs)


print(kwargs_function(name="Alex", age=34, city="Berlin"))


def function_for_all_args(x: int, y: int, *args, j: int = 77, **kwargs):
    print(x, y)
    print(args)
    print(j)
    print(kwargs)


one_person = {
    "name": "John",
    "surname": "Connor",
    "city": "New York",
    "age": 16
}
print(function_for_all_args(1, 6, 6, 7, 8, **one_person))


# return several values. returns tuple
def modify_dict(old_dict: dict, **kwargs) -> tuple[dict, bool]:  # square brackets here!
    is_modified = False
    for key, value in kwargs.items():
        if old_dict.get(key) != value:
            old_dict[key] = value
            is_modified = True

    return old_dict, is_modified

