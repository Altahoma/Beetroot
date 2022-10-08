def in_range(start, end, step=1):
    i = start

    if step == 0:
        raise ValueError
    if step > 0:
        while i < end:
            yield i
            i += step
    if step < 0:
        while i > end:
            yield i
            i += step


if __name__ == '__main__':
    assert list(in_range(0, 10)) == list(range(0, 10))
    assert list(in_range(-5, 10)) == list(range(-5, 10))
    assert list(in_range(0, 10, 2)) == list(range(0, 10, 2))
    assert list(in_range(0, 10, -2)) == list(range(0, 10, -2))
    assert list(in_range(0, -10, -1)) == list(range(0, -10, -1))
    assert list(in_range(-5, -10, -1)) == list(range(-5, -10, -1))
