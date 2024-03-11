"""EX05 Dictionary Utility Functions - Count!"""
__author__ = "730711248"


def count(list1: list[str]) -> dict[str, int]:
    """Creates dictionary that shows number of apperances!"""
    dict1: dict[str, int] = {}
    for elem in list1:
        if elem in dict1:
            dict1[elem] += 1
        else:
            dict1[elem] = 1
    return dict1