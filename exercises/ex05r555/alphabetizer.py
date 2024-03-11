"""EX05 Dictionary Utility Functions - Alphabetizer!"""
__author__ = "730711248"


def alphabetizer(list1: list[str]) -> dict[str, list[str]]:
    """Sorts list into alphabitized dictionary!"""
    dict1: dict[str, list[str]] = {}
    for elem in list1:
        word: str = elem.lower()
        if word[0] in dict1:
            dict1[word[0]] = [dict1[word[0]], elem]
        else:
            dict1[word[0]] = elem
    return dict1