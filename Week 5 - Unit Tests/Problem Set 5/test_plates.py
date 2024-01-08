from plates import is_valid


# Check if the length is between 2 - 6
def test_length():
    assert is_valid("s") == False
    assert is_valid("testing") == False
    assert is_valid("plat3") == True


# Check if first two character are not digits
def test_digits():
    assert is_valid("B9999") == False
    assert is_valid("5434") == False


# Check if there is characters different than letters and numbers
def test_punctuation():
    assert is_valid("word.") == False
    assert is_valid("wo?rd") == False
    assert is_valid("wo rd") == False


# Check if:
def test_digits_position():
    assert is_valid("AAA222") == True  # digits appear at the end of string
    assert is_valid("AAA22A") == False  # letters don't appear after digits
    assert is_valid("AA022") == False  # 0 is not the first digit
