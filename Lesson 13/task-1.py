def count_variables(foo):
    return foo.__code__.co_nlocals


def my_func():
    first_var = 2
    second_var = 4.2
    third_var = 'hello'


print(count_variables(my_func))
