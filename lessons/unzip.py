"""Splitting a dictionary into two lists!"""
__author__ = "730711248"


def get_keys(dict: dict[str, int]) -> list[str]:
    """Given get_keys, create a list of the keys."""
    key_list: list[str] = []
    for key in dict:
        key_list.append(key)
    return key_list


def get_values(dict: dict[str, int]) -> list[int]:
    """Given get_values, create a list of the values."""
    value_list: list[int] = []
    for key in dict:
        value_list.append(dict[key])
    return value_list