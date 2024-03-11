my_set = {1, 4, 7, 9, 64}  # like in dict, but not key: value. only uniq elements, unordered

my_func_set = set()
for i in range(6):
    my_func_set.add(i ** 3)

print(my_func_set)
print(type(my_func_set))  # type is set

print(my_set.intersection(my_func_set))
print(my_set.difference(my_func_set))
