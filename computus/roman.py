def arabic_to_roman(num: int) -> str:
    """Convert integer to Roman numeral."""

    if not (0 < num < 4000):
        raise ValueError("Number must be between 1 and 3999")

    roman_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    result = []
    for value, symbol in roman_map:
        while num >= value:
            result.append(symbol)
            num -= value

    return "".join(result)