import art


def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1-n2

def multiple(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {
    "+" : add,
    "_" : subtract,
    "*" : multiple,
    "/" : divide
}
def calculator():
    print(art.logo)
    should_accumulate = True
    first_number = float(input("Enter the first number to perform the operations"))
    while should_accumulate:

        for operator in operations:
            print(operator)
        operation_selected = input('selected operation of "+", "-", "*" or "/")')
        second_number = float(input("Enter the second number to perform the operations"))
        print(first_number,second_number)
        result = (operations[operation_selected](first_number,second_number))
        print(f"{first_number} {operation_selected}{second_number} = {result}")

        proceed = input("if you want proceed with another operations press 'y' or 'n'  to restart  ").lower()
        if proceed == 'y':
             first_number = result

        else:
             should_accumulate =False
             print("\n"*20)
             calculator()
calculator()





