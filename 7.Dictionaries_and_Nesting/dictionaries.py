my_dict = {
    "hello": "World",
    123: "Morning"
}

print(my_dict["hello"])
print(my_dict[123])

# Add item
my_dict["new"] = "Item"
print(my_dict)

new_dict = {}

# my_dict = {}
# print(my_dict)

my_dict["hello"] = "People"
print(my_dict)

# Loop through
for key in my_dict:
    print(my_dict[key])
