from functools import wraps


class TypeDecorators:
    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(arg):
            return int(func(arg))

        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(arg):
            return str(func(arg))

        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(arg):
            return bool(func(arg))

        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(arg):
            return float(func(arg))

        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_str
def do_anything(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


@TypeDecorators.to_float
def do_thing(string: str):
    return string


assert do_nothing.__name__ == 'do_nothing'  # check @wraps
assert do_nothing('25') == 25  # to int
assert do_anything(False) == 'False'  # to str
assert do_something('True') is True  # to bool
assert do_thing('4.2') == 4.2  # to float
