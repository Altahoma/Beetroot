def oops():
    raise IndexError


def call_oops():
    try:
        oops()
    except IndexError:
        print('In python, the indexing starts from 0.')


call_oops()
