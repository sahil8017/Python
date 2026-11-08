logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------.
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
|_____________________|
"""
print(logo)

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def divide(a,b):
    return a/b
def multiply(a,b):
    return a*b

number1 = float(input("What's the first number?: "))

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
for operation in operations:
    print(operation)

operator = input("Pick an operation: ")
number2 = float(input("What's the next number? "))
result = operations[operator](number1, number2)

print(f"{number1} {operator} {number2} = {result}")

while True:
    continue_calculation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if continue_calculation == "y":
        number1 = result
        operator = input("Pick an operation: ")
        number2 = float(input("What's the next number? "))
        result = operations[operator](number1, number2)
        print(f"{number1} {operator} {number2} = {result}")
    else:
        print("Goodbye!") 
        break       