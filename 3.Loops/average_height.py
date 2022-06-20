# using for loop

students_height = input("Whats the students height?").split()

for n in range(0, len(students_height)):
    students_height[n] = int(students_height[n])

print(students_height)
total = 0
length = 0

for num in students_height:
    total += num
    length += 1

average = total/length
print(f"Average of the {students_height} is {average}")
