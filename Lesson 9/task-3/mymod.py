def count_lines(name):
    with open(name) as file:
        total_lines = len(file.readlines())
        return total_lines


def count_chars(name):
    with open(name) as file:
        total_chars = len(file.read())
        return total_chars


def test(name):
    return [count_lines(name), count_chars(name)]
