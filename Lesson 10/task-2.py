def divided_square():
    a = int(input('Enter first number: '))
    b = int(input('Enter first number: '))

    return a**a / b


try:
    print(divided_square())
except ValueError:
    print('Supported only numbers.')
except ZeroDivisionError:
    print('Cannot divide by zero.')
