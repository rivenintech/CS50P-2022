from jar import Jar
from pytest import raises


def test_init():
    jar = Jar(10)
    assert jar._capacity == 10
    assert jar.cookies == 0

    # Test default value
    jar = Jar()
    assert jar._capacity == 12
    assert jar.cookies == 0

    with raises(ValueError):
        jar = Jar("not int")

    # Test negative int
    with raises(ValueError):
        jar = Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(6)
    assert jar.cookies == 6

    with raises(ValueError):
        jar.deposit(7)


def test_withdraw():
    jar = Jar()
    jar.deposit(6)
    jar.withdraw(3)
    assert jar.cookies == 3

    with raises(ValueError):
        jar.withdraw(10)
