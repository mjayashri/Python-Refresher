# Ask ur list of 3 friends
# each friend, we tell  if they are same city
# each nearby friends we ll save in nearby friends
friends = input("Enter 3 friends name separated by comma(no spaces plz): ").split(",")

people = open("people.txt", "r")
people_nearby = [line.strip() for line in people.readlines()]

people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)

friends_nearby = friends_set.intersection(people_nearby_set)

friends_nearby_file = open("nearby_friends.txt" , "w")

for friend in friends_nearby:
    print(f"{friend} is nearby, please visit him")
    friends_nearby_file.write(f'{friend}\n')

friends_nearby_file.close()
