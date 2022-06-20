import random

names_string = input("Give me everybody's names, separated by comma \n")
names = names_string.split(", ")

print(names)

names_length = len(names)

random_choice = random.randint(0, names_length-1)
selected_name = names[random_choice]

print(f"{selected_name} is going to pay the bill")

selected_person = random.choice(names)

print(f"{selected_person} is going to pay the bill using choice method")