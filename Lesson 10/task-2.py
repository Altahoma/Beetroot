def divided_square():
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))

    return a**2 / b


try:
    print(divided_square())
except ValueError:
    print('Supported only numbers.')
except ZeroDivisionError:
    print('Cannot divide by zero.')
