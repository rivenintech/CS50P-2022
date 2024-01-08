from twttr import shorten


# Testing word that contain vowels
def test_with_vowels():
    assert shorten("random word") == "rndm wrd"
    assert shorten("another word") == "nthr wrd"


# Testing words that don't contain any vowels
def test_without_vowels():
    assert shorten("glyph") == "glyph"
    assert shorten("hymn") == "hymn"


# Testing words with mixed letter case
def test_mixed_case():
    assert shorten("RanDom wORd") == "RnDm wRd"
    assert shorten("GLyPh") == "GLyPh"


# Testing words with numbers
def test_numbers():
    assert shorten("RanDom 1 wORd 23") == "RnDm 1 wRd 23"
    assert shorten("GL12yPh") == "GL12yPh"


# Testing words with punctuation
def test_punctuation():
    assert shorten("Hello, world") == "Hll, wrld"
    assert shorten("He.llo , world") == "H.ll , wrld"
