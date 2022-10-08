def with_index(iterable, start=0):
    n = start
    for element in iterable:
        yield n, element
        n += 1


if __name__ == '__main__':
    my_list = ['a', 'b', 'c', 'd', 'e']

    print(list(with_index(my_list)))
    print(list(list(with_index(my_list, 10))))
