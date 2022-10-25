def is_palindrome(looking_str: str, index: int = 0) -> bool:
    if index > len(looking_str) // 2:
        return True
    if looking_str[index] != looking_str[-index - 1]:
        return False
    return is_palindrome(looking_str, index + 1)


if __name__ == "__main__":
    assert is_palindrome("o")
    assert is_palindrome("gg")
    assert not is_palindrome("wp")
    assert not is_palindrome("hello")
    assert is_palindrome("nolemon-nomelon")
