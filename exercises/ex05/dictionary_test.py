"""EX06 - `dict` Unit Tests!"""
__author__ = "730711248"

from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest


# invert function tests
def test_invert_empty_dict() -> None:  # edge case
    """Invert of an empty list should return an empty list."""
    assert invert({}) == {}


def test_dict_length_3() -> None:  # use case
    """Given four values should return an inverted list."""
    assert invert({"1st key -> value": "1st value -> key", "2nd key -> value": "2nd value -> key", "3rd key -> value": "3rd value -> key"}) == {"1st value -> key": "1st key -> value", "2nd value -> key": "2nd key -> value", "3rd value -> key": "3rd key -> value"}


def test_same_key() -> None:  # use case
    """Given dict with same values->key raise KeyError."""
    with pytest.raises(KeyError):
        dict1 = {"pie": "strawberry", "cake": "strawberry"}
        invert(dict1)


def test_dict_bools() -> None:  # edge case
    """Given dict of bools, return inverted dict."""
    assert invert({1.0: 1.1, 2.0: 2.2, 3.0: 3.3}) == {1.1: 1.0, 2.2: 2.0, 3.3: 3.0}


# favorite_color unit tests
def test_one_color() -> None:  # use case
    """Given only one color dict return that color."""
    assert favorite_color({"color": "purple"}) == "purple"


def test_color_empty_dict() -> None:  # edge case
    """Given an empty dict, return an empty string as favorite color."""
    assert favorite_color({"": ""}) == ""


def test_color_tie() -> None:  # use case
    """Given a tie for favorite color, return the color that appeared first."""
    assert favorite_color({"one": "pink", "two": "pink", "three": "purple", "four": "purple"}) == "pink"


# count unit tests
def test_list_ints() -> None:  # edge case
    """Given a list of ints, return count of those ints."""
    assert count([1, 2, 3]) == {1: 1, 2: 1, 3: 1}


def test_same_str() -> None:  # use case
    """Given list of same word, return the number of times word is in list."""
    assert count(["cake", "cake", "cake"]) == {"cake": 3}


def test_one_str() -> None:  # use case
    """Given one str return count of one for that string."""
    assert count(["strawberry"]) == {"strawberry": 1}


def test_counter_empty_list() -> None:  # edge case
    """Given empty list, return empty dict."""
    assert count([]) == {}


# alphabetizer unit test
def test_capital_words() -> None:  # use case
    """Given capital words, should add to lowercase letter dict."""
    assert alphabetizer(["shell", "Strawberry", "Blueberry", "bell"]) == {"s": ["shell", "Strawberry"], "b": ["Blueberry", "bell"]}


def test_diff_letter() -> None:  # use case
    """Given different first letters, return dict with each letter as a diff key."""
    assert alphabetizer(["alpaca", "bunny", "cat"]) == {"a": ["alpaca"], "b": ["bunny"], "c": ["cat"]}


def test_same_word() -> None:  # edge case
    """Given list of same word, return dict of only that word."""
    assert alphabetizer(["strawberry", "strawberry", "strawberry"]) == {"s": ["strawberry", "strawberry", "strawberry"]}


def test_empty_list() -> None:  # edge case
    """Given an empty list, return an empty dict."""
    assert alphabetizer([]) == {}


# update_attendance unit tests
def test_new_day() -> None:  # use case
    """Given a new day, return dict including new key of that day."""
    test_dict: dict[str, list[str]] = {"Monday": ["Lilo", "Stitch"], "Tuesday": ["Stitch"]}
    update_attendance(test_dict, "Wednesday", "Lilo") 
    assert test_dict == {"Monday": ["Lilo", "Stitch"], "Tuesday": ["Stitch"], "Wednesday": ["Lilo"]}


def test_same_day() -> None:  # use case
    """Given day that already in dict, append the names to the list of that day."""
    test_dict: dict[str, list[str]] = {"Monday": ["Eeyore", "Piglet"]}
    update_attendance(test_dict, "Monday", "Pooh") 
    assert test_dict == {"Monday": ["Eeyore", "Piglet", "Pooh"]}


def test_attendance_empty_list() -> None:  # edge case
    """Given empty parameters, return an dict of empty strings."""
    test_dict: dict[str, list[str]] = {}
    update_attendance(test_dict, "", "") 
    assert test_dict == {"": [""]}