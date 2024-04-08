# Calculator
 
from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def minus(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 * n2

operations = {
    "+": add,
    "-": minus,
    "*": multiply,
    "/": divide,
}

n1 = float(input("What's the first number? "))
n2 = float(input("What's the second number? "))
for symbol in operations:
    print(symbol)
should_continue = True    

while should_continue:
    operation_symbol = input("Pick an operation from the line above: ")
    calculation_function = operations[operation_symbol]
    answer = calculation_function(n1, n2)

    print(f"{n1} {operation_symbol} {n2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit.: ") == "y":
        n1 = answer
    else:
        should_continue = False