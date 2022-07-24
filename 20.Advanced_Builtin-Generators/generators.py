class FirsHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

    def __iter__(self):
        return self


my_gen = FirsHundredGenerator()
print(my_gen)
print(next(my_gen))
print(next(my_gen))

# iterator vs iterable

# class FirstHundredIterable:
#     def __iter__(self):
#         return FirsHundredGenerator()


print(FirsHundredGenerator())

for i in FirsHundredGenerator():
    print(i)


class FirstFiveIterator:
    def __init__(self):
        self.numbers = [1, 2, 3, 4, 5]
        self.i = 0

    def __next__(self):
        if self.i < len(self.numbers):
            current = self.numbers[self.i]
            self.i += 1
            return current
        else:
            raise StopIteration()


class AnotherIterable:
    def __init__(self):
        self.cars = ["fiesta", "Focus"]

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, item):
        return self.cars[item]


for car in AnotherIterable():
    print(car)

my_num = [x for x in [1, 2, 3, 4, 5]]

my_num_gen = (x for x in [1, 2, 3, 4, 5])
print(next(my_num_gen))
