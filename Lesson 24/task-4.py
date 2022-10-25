def reverse(input_str: str) -> str:
    if len(input_str) == 1:
        return input_str
    return reverse(input_str[1:]) + input_str[0]


if __name__ == "__main__":
    assert reverse("hello") == "olleh"
    assert reverse("o") == "o"
    assert reverse("banana") == "ananab"
