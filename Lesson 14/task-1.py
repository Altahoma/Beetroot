def logger(func):
    def wrapper(*args):
        print(f'{func.__name__} called with {args}')
        return func(*args)
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


print(add(4, 5))
print()
print(square_all(1, 2, 3, 4, 7))