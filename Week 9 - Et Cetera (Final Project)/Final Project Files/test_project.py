import pytest

from project import get_quote, edit_background

# I can't really test any of the functions because they need Pexels API key to work, that I don't think I should publish. :(

def test_edit_background():
    assert edit_background() == True

def test_get_quote():
    assert isinstance(get_quote(), tuple)