ROMAN = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]


class RomanNumerals:
    @staticmethod
    def to_roman(val: int) -> str:
        result = ""
        for arabic, roman in ROMAN:
            factor, val = divmod(val, arabic)
            result += roman * factor
        return result

    @staticmethod
    def from_roman(roman_num: str) -> int:
        arabic = {roman: arabic for arabic, roman in ROMAN[::-1]}
        total = 0
        prev = 0
        for char in roman_num[::-1]:
            current = arabic[char]
            if current >= prev:
                total += current
            else:
                total -= current
            prev = current
        return total


assert RomanNumerals.to_roman(3999) == "MMMCMXCIX"
assert RomanNumerals.to_roman(1950) == "MCML"
assert RomanNumerals.to_roman(1890) == "MDCCCXC"

assert RomanNumerals.from_roman("MCMLIV") == 1954
assert RomanNumerals.from_roman("MDCCCXC") == 1890
assert RomanNumerals.from_roman("V") == 5
