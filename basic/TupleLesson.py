# unmodifiable. Everything else: same as list
user_roles = ("admin", "editor", "viewer", "auditor", "devops")

print(f"Len is: {len(user_roles)}")

for role in user_roles:
    print(f"Role: {role} in {user_roles.index(role)} position")

not_tuple = ("someRole")
print(type(not_tuple))  # returns string type
is_tuple = ("someRole",)  # WITH COMMA!
print(type(is_tuple))  # now, returns tuple

# unpacking the tuple (list too). Number of vars should be equal to tuple size
role_1, role_2, role_3, role_4, _ = user_roles  # underscore means skip value
print(role_1)
print(role_2)
print(role_3)

