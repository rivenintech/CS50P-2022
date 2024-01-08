from numb3rs import validate


def test_valid():
    assert validate("192.168.0.1") == True
    assert validate("1.2.3.4") == True
    assert validate("127.0.0.1") == True
    assert validate("12.13.14.15") == True


def test_invalid():
    assert validate("100.120.3.1.12") == False
    assert validate("100.120.1") == False
    assert validate("256.256.256.256") == False
    assert validate("1.2.260.270") == False
    assert validate("dog.dog.dog.dog") == False
    assert validate("This is ip 192.168.0.1") == False
