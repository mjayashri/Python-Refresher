accounts = {
    'checking': 15596.00,
    'saving': 1234.00
}


def add_balance(amount: float, name: str = 'checking') -> float:
    """
    :param amount:
    :param name:
    :return: new balance
    """
    accounts[name] += amount
    return accounts[name]


transactions = [
    (-150.89, 'checking'),
    (250.89, 'checking'),
    (10.89, 'saving'),
    (1550.89, 'checking'),
    (-160.89, 'saving'),
    (-150.59, 'checking')
]

for t in transactions:
    # print(add_balance(*t))
    print(add_balance(amount=t[0], name=t[1]))
    # add_balance(t[0], t[1])


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


usersList = [
    {'username': 'rolf', 'password': '123'},
    {'username': 'jayashri', 'password': '123'}
]

# user_objects = [User(u['username'], u['password']) for u in usersList]

user_objects = [ User(**data) for data in usersList]

# print(user_objects)

usersList_2 = [
    ( 'rolf',  '123'),
    ('jayashri', '123')
]

user_objects_2 = [ User(*data) for data in usersList_2]

















