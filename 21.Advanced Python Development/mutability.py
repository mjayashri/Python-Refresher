my_dict = {
    "Hello": "world",
    "Happy": "coding"
}

new_dict = my_dict  # both same dict

print(id(my_dict))  # different

my_dict = {
    "Hello": "world",
    "Happy": "coding"
}
print(id(my_dict))

my_dict["Hello"] = "People"

print(id(my_dict))

# integers are immutable, also tuple floats and strings
my_int = 5
print(id(my_int))  # different
my_int = my_int + 1
print(id(my_int))  # different

# lists are mutable
friends = ["Jayashri", "Rahul"]

print(id(friends))  # same

friends.append("Charan")

print(id(friends))  # same
