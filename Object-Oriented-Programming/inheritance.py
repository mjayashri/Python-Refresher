class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    @property
    def weekly_salary(self):
        return self.salary * 31


david = WorkingStudent("David", "MIT", 25)

print(david.salary)
david.marks.append(76)
david.marks.append(96)

print(david.average())

print(david.salary)
print(david.weekly_salary)
