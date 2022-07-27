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


add_balance(500)

print(accounts['checking'])

# Mutable default arguments - bad idea

