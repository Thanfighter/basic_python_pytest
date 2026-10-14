import pytest
from toolkit.text_utils import reverse_text, is_palindrome, count_words


def test_reverse_text():
    assert reverse_text("hello") == "olleh"


def test_reverse_empty_string():
    assert reverse_text("") == ""


@pytest.mark.parametrize(
    "text, expected",
    [
        ("racecar", True),
        ("Racecar", True),
        ("A man, a plan, a canal: Panama", True),
        ("hello", False),
        ("", True),
    ],
)
def test_is_palindrome(text, expected):
    assert is_palindrome(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello world", 2),
        ("one", 1),
        ("", 0),
        ("  lots   of   spaces  ", 3),
    ],
)
def test_count_words(text, expected):
    assert count_words(text) == expected