# using for loop
students_scores = input("input the list of students scores?").split()

for n in range(0, len(students_scores)):
    students_scores[n] = int(students_scores[n])

highest_score = 0
for score in students_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")
