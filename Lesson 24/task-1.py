from typing import Union


def to_power(x: Union[int, float], exp: int) -> int | float:
    if exp < 0:
        raise ValueError("This function works only with exp >= 0.")
    if exp == 0:
        return 1
    return x * to_power(x, exp - 1)


if __name__ == "__main__":
    assert to_power(6, 0) == 1
    assert to_power(4, 1) == 4
    assert to_power(2, 3) == 8
    assert to_power(3.5, 2) == 12.25
    assert to_power(5, 3) == 125
