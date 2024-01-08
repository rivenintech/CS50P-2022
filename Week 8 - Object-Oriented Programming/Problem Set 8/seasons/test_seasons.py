from seasons import get_datetime_obj, minutes_as_words
from datetime import date


def test_get_datetime_obj():
    get_datetime_obj("word-instead-of-date") == False
    get_datetime_obj("99-1-1") == False
    get_datetime_obj("2023-04-18") == date(2023, 4, 18)
