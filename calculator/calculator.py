def calculator():
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        return x / y

    def square(x, y):
        return x ** y
    user_choice = True
    while user_choice:
        num1 = float(input('Please input your first number : '))
        operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '**': square,
        }
        for symbols in operations:
         print(symbols)
        operation_symbol = str(input('please enter your symbol : '))
        num2 = float(input('Please input your first number : '))
        answer = operations[operation_symbol](num1, num2)
        print(answer)
        user_input = str(input("To continue enter 'yes' or press enter to end : ")).lower()
        if user_input == 'yes':
            num1 = answer
        else:
            user_choice = False
            break


calculator()