friends = ['Jayashri', 'Rahul', 'Dravid', 'William', 'Ravi']

friends_lower = map(lambda x: x.lower(), friends)
print(list(friends_lower))

friends_lower = [friend.lower() for friend in friends]
print(friends_lower)

friends_lower = (friend.lower() for friend in friends)
print(list(friends_lower))


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data["username"], data['password'])


usersList = [
    {'username': 'rolf', 'password': '123'},
    {'username': 'jayashri', 'password': '123'}
]

# users = [User.from_dict(user) for user in usersList]
users = map(User.from_dict, usersList)
