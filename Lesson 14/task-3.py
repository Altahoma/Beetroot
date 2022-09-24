def arg_rules(type_: type, max_length: int, contains: list):
    def check_rules(func):
        def wrapper(arg):
            if type(arg) != type_:
                print(f'Wrong type: {type(arg)} instead {type_} ')
                return False
            elif len(arg) > max_length:
                print(f'The length of \'{arg}\' is more than allowed: max={max_length}')
                return False
            elif any(symbols not in arg for symbols in contains):
                print(f'Do not contain needed symbols: {", ".join(contains)}')
                return False
            else:
                print('All checks passed')
                return func(arg)
        return wrapper
    return check_rules


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan(42) is False
assert create_slogan('something') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
