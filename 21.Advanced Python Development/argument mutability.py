friends_last_seen = {
    'Jayashri': 28,
    'Rahul': 45,
    'Vikram': 22
}


def see_friend(friends, name):
    print(id(friends))
    print(friends is friends_last_seen) # check ids
    friends[name] = 10


print(id(friends_last_seen))
print(f"id(friends_last_seen['Rahul']) : {id(friends_last_seen['Rahul'])} ")
see_friend(friends_last_seen, 'Rahul')
print(f"id(friends_last_seen['Rahul']) : {id(friends_last_seen['Rahul'])} ")
print(id(friends_last_seen))

