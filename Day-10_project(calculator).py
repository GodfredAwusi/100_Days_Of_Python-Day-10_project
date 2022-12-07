# Calculator
from art import logo

# Add function
def add(num1, num2):
    return num1 + num2

# Subtract function
def sub(num1, num2):
    return num1 - num2

# Multiply function
def mul(num1, num2):
    return num1 * num2

# Divide function
def div(num1, num2):
    return num1 / num2

# Dictionary of the operation functions
operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

# More operations condition

def calculator():
    print(logo)

    stop_operations = False
    # first number input
    first_number = float(input("What's the first number?: "))

    # Printing the operators
    for operator in operations:
        print(operator)
    # While loop to make more operations possible
    while not stop_operations:
        # User operator choice
        operation_symbol = input("Pick an operator: ")
        # Second number input
        next_number = float(input("What's the next?: "))

        # Function to call the required operation function
        calculation_function = operations[operation_symbol]
        # Parsing the number inputs to the calculation function
        answer = calculation_function(first_number, next_number)
        # Printing the operation and result
        print(f"{first_number} {operation_symbol} {next_number} = {answer} ")

        # More operations with answer option
        more_operations = input(f"Type 's' to start a new calculation or 'y' to continue calculating with {answer} else type 'n' to exit or : ").lower()

        if more_operations == "y":
            first_number = answer
        elif more_operations == "n":
            stop_operations = True
        elif more_operations == "s":
            calculator() # Recursion - calling a function withing its own definition

calculator()
