for number in range(0, 11, 3):
    print(number)

# sum of all even numbers
even = 0
for number in range(1, 101):
    if number % 2 == 0:
        even += number

print(f"sum of all even numbers between 0 to 100 is {even}")