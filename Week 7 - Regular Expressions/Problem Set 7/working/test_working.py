from working import convert
from pytest import raises


def test_valid():
    assert convert("10 AM to 5 PM") == "10:00 to 17:00"
    assert convert("3 AM to 11 AM") == "03:00 to 11:00"
    assert convert("4:15 AM to 11:20 AM") == "04:15 to 11:20"


def test_invalid_format():
    with raises(ValueError):
        convert("10 AM - 5 PM")
    with raises(ValueError):
        convert("9:1 AM - 4:5 PM")
    with raises(ValueError):
        convert("9AM to 4PM")
    with raises(ValueError):
        convert("9 to 4")


def test_invalid_digits():
    with raises(ValueError):
        convert("3:60 AM to 4:60 PM")
    with raises(ValueError):
        convert("13:00 AM to 14:00 PM")
    with raises(ValueError):
        convert("13 AM to 14 PM")
