from bank import value


def test_rewards():
    assert value("hello") == 0
    assert value("hi") == 20
    assert value("good morning") == 100


# Test greetings with mixed letter cases
def test_mixed_letter_case():
    assert value("HeLLo") == 0
    assert value("Hi") == 20
    assert value("GOOD mOrnIng") == 100
