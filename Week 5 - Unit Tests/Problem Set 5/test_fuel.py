from fuel import convert, gauge
from pytest import raises


def test_convert():
    with raises(ValueError):  # Invalid format, not integers
        convert("hello")
    with raises(ValueError):  # Valid format, not integers
        convert("hello/world")
    with raises(ValueError):  # Invalid format, integers
        convert("1")
    with raises(ValueError):  # X bigger than Y
        convert("2/1")
    with raises(ZeroDivisionError):  # Y is 0
        convert("0/0")

    assert convert("1/2") == 50


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(75) == "75%"
