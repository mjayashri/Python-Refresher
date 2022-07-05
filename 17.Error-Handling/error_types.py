# Index error
friends = ["Apple", "Orange"]
# friends[2] # out of index error

# key error
# eg. when key is not available in the dictionary
my_dict = {"hello": "Jayashri"}
# print(my_dict["hi"])

# name error
# print(joy) #joy not defined

# Attribute error -  when the object has no attribute
friends_nearby = ["Jerry"]


# friends.intersection(friends_nearby) #list has no intersection attribute

# Not implemented error - yu can use to raise error
def login():
    raise NotImplementedError("This feature not implemented error")

# login()

# RunTime error - happens when running code
# This will be base error

# Syntax error
# def hello: # () is missing
#     return "Hi"

# indentation error

# Tab error
# indented body have four spaces (mix and match indentation types)

# Type Error
# "hi" + 5  # => Type error

# Value error
# int("20.5") =>20.5 is not int after casting

# Import Error
# cyclic imports

# Deprecation warning
# No longer the best way of doing
# raise DeprecationWarning("Warning!")


















