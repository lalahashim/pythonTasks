import day10aer

def add(n1, n2):
    return n1+n2
def substract(n1,n2):
    return n1-n2
def multiply(n1, n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations = {"+": add, 
            "-": substract, 
            "*": multiply, 
            "/": divide
            }
    
def calculator():
    print(day10aer.logo)

    first_num = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_choice = input("Pick an operation: ")
        second_num = float(input("What's the next number? "))

        calculation_function = operations[operation_choice]
        answer = calculation_function(first_num, second_num)

        print(f"{first_num} {operation_choice} {second_num} = {answer}")

        another_calc = input(f"Type 'yes' to continue calculating with {answer}, or type 'no' to start a new calculation: ")
        if another_calc == 'yes':
            first_num = answer
        else:
            should_continue = False
            calculator()

calculator()