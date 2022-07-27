friends = [
    {
        "name": "Jayashri",
        "location": "Chennai"
    },
    {
        "name": "Kishore",
        "location": "Chennai"
    },
    {
        "name": "John",
        "location": "Bangalorei"
    },
    {
        "name": "Malini",
        "location": "Delhi"
    }
]

your_location = input("Where are you now? : ")

friends_nearby = [friend for friend in friends if friend['location'] == your_location]

if any(friends_nearby):
    print("You have a friend near by!!")

# all
print(all([1, 2, 3, 4, 5]))
print(all([1, 2, 3, 4, 5, 0]))
