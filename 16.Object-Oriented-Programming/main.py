my_student = {
    'name': 'Rolf Smith',
    'grades': [70, 80, 90, 99]
}


def average_grade():
    return sum(my_student['grades']) / len(my_student['grades'])


print(average_grade())


class Student:
    def __init__(self, new_name, new_grade):
        self.name = new_name
        self.grades = new_grade

    def average(self):
        return sum(self.grades) / len(self.grades)


std_one = Student("M Jayashri", [70, 90, 80, 95])
std_two = Student("Kevin", [60, 90, 90, 95])

print(std_one.name)
print(std_two.name)

print(std_one.__class__)

print(std_one.average())
