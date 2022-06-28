class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f"<Fixed Float {self.amount:.2f}>"

    @classmethod
    def from_sum(cls, value_1, value_2):
        return cls(value_1 + value_2)


# number = FixedFloat(13.45667)
new_number = FixedFloat.from_sum(14.566, 345.7778)
print(new_number)


class Dollar(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '$'

    def __repr__(self):
        return f"<Dollar {self.symbol} {self.amount:.2f}>"


money = Dollar(45.66)
print(money)

money_1 = Dollar.from_sum(12.34, 45.23)
print(money_1)
