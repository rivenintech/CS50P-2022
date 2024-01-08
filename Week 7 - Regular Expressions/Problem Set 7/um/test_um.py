from um import count


def test_letter_case():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2


def test_in_words():
    assert count("yummy, yum, yum") == 0
    assert count("instrumental") == 0


def test_special_chars():
    assert count("um um, um?") == 3
    assert count("Uhm, um. Um, um!") == 3
