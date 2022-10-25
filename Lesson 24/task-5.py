def sum_of_digits(digit_string: str) -> int:
    if not digit_string.isdigit():
        raise ValueError("input string must be digit string")
    if len(digit_string) == 1:
        return int(digit_string)
    return int(digit_string[0]) + sum_of_digits(digit_string[1:])


if __name__ == "__main__":
    assert sum_of_digits("26") == 8
    assert sum_of_digits("1337") == 14
    assert sum_of_digits("0801") == 9
