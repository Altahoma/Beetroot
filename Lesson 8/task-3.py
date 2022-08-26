def make_operation(operator, *args):
    total = args[0]

    if operator == '+':
        for num in args[1:]:
            total += num
    elif operator == '-':
        for num in args[1:]:
            total -= num
    elif operator == '*':
        for num in args[1:]:
            total *= num

    return total


print(make_operation('+', 7, 7, 2))  # return 16
print(make_operation('-', 5, 5, -10, -20))  # return 30
print(make_operation('*', 7, 6))  # return 42
