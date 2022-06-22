def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = float(input("Whats the first number: "))
num2 = float(input("Whats the second number: "))

print("which of the operation to be performed?")
for operand in operations:
    print(operand)

operator_chosen = input("Pick any one of the above operations?: ")

function_to_be_called = operations[operator_chosen]

answer = function_to_be_called(num1, num2)

print(f"{num1} {operator_chosen} {num2} = {answer}")
