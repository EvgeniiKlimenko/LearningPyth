from copy import deepcopy

person = {
    "name": "John",
    "surname": "Connor",
    "city": "New York",
    "age": 16
}

print(person)
person["job"] = "engineer"  # add pair
print(person)
other_person = {}  # empty dict
#print(person["country"])  # non-existing key => exception. use next instead
print(person.get("country"))  # return NONE instead
print(person.get("country", "USA"))  # return default value USA if no such key

# iteration, bad version
for value in person:
    print(value)  # will return only keys here
    print(person[value])  # will return values

# iteration, better version
for item in person.items():
    print(item)  # item is a tuple
    print(type(item))  # type it tuple (key: value)

# iteration, the best version
for key, value in person.items():
    print(f"Key is {key} with value: {value}")

for key in person.keys():  # also there is person.values() for values
    print(f"Only keys: {key}")

one_person = {
    "name": "John",
    "surname": "Connor",
    "city": "New York",
    "age": 16
}

two_person = {
    "surname": "Connor",
    "name": "John",
    "age": 16,
    "city": "New York"
}
print(one_person == two_person)  # will return True. Order of pairs does not matter.

additional_info = {
    "country": "Connor",
    "job": "engineer",
    "city": "New York",
    "licence": True
}

# concatenate two dicts
one_person.update(additional_info)  # second one overwrites values (by the same keys) of the first.
print(one_person)

# copy a dict to create an independent copy of dict
#copied_dict = additional_info.copy()  # will NOT work with mutable objects inside a dict, list, set for example
copied_dict = deepcopy(additional_info)  # better to use copy.deepcopy
copied_dict["job"] = "Pilot"
print("Dictionary original: ", additional_info)
print("Copy is: ", copied_dict)
