def oops():
    lst = [1, 2, 3]
    print(lst[3])


def call_oops():
    try:
        oops()
    except IndexError:
        print('In python , the indexing starts from 0.')


call_oops()
