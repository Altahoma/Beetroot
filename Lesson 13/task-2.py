def func_outside():
    def func_inside():
        print('hello from inside func')
    return func_inside


my_func = func_outside()
my_func()
