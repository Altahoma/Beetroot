def mult(a: int, b: int) -> int:
    if b < 0 or a < 0:
        raise ValueError("This function works only with positive integers")
    if a == 0 or b == 0:
        return 0
    return a + mult(a, b - 1)


if __name__ == "__main__":
    assert mult(2, 2) == 4
    assert mult(2, 4) == 8
    assert mult(2, 0) == 0
    assert mult(2, 21) == 42
