"""Test my garden functions."""
__author__ = "730711248"

from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date
import pytest


# unit tests for add_by_kind

def test_empty_dict() -> None:  # use case
    """Given an empty dict still append the parameters."""
    test_by_kind: dict[str, list[str]] = {}
    add_by_kind(test_by_kind, "flower", "lavender")
    assert test_by_kind == {'flower': ['lavender']}


def test_empty_parameters() -> None:  # edge case
    """Given empty parameters append empty strings."""
    test_by_kind: dict[str, list[str]] = {}
    add_by_kind(test_by_kind, "", "")
    assert test_by_kind == {'': ['']}


# unit tests for add_by_date

def test_new_month() -> None:  # use case
    """Given new month make new key for that month."""
    garden_by_date: dict[str, list[str]] = {"November": ["lily"], "December": ["spinach"]}
    add_by_date(garden_by_date, "January", "peas")
    assert garden_by_date == {"November": ["lily"], "December": ["spinach"], "January": ["peas"]}


def test_dict_with_int() -> None:  # edge case
    """Given int in dict parameter, dict has int key."""
    garden_by_date: dict[str, list[str]] = {1: ["lavender"]}
    add_by_date(garden_by_date, "January", "peas")
    assert garden_by_date == {1: ["lavender"], "January": ["peas"]}


# unit tests lookup_by_kind_and_date

def test_kind_not_in() -> None:  # use case
    """If kind not in plants_by_kind, raise error."""
    with pytest.raises(AssertionError):
        plants_by_kind: dict[str, list[str]] = {"flower": ["lavender", "lily"]}
        plants_by_date: dict[str, list[str]] = {"November": ["lily"], "December": ["spinach"]}
        lookup_by_kind_and_date(plants_by_kind, plants_by_date, "vegetable", "June")


def test_empty_kind() -> None:  # edge case
    """Given an empty list in plants_by_kind, return no kind in month."""
    plants_by_kind: dict[str, list[str]] = {"flower": []}
    plants_by_date: dict[str, list[str]] = {"November": ["lily"], "December": ["spinach"]}
    assert lookup_by_kind_and_date(plants_by_kind, plants_by_date, "flower", "November") == "No flowers to plant in November."