"""EX04 list Utility Functions!"""
__author__ = "730711248"


def all(list: list[int], int: int) -> bool:
    """Given all, return a bool based on if the list is equal to the integer!"""
    if len(list) == 0:  # if list is empty
        return False
    for elem in list:
        if elem != int:  # if elem is not the same as the integer
            return False
    return True


def max(list: list[int]) -> int:
    """For max, return the integer that is the largest number in the list."""
    if len(list) == 0:
        raise ValueError("max() arg is an empty List")  # empty list
    largest_number: int = -110  # -110 is a placeholder
    for elem in list:
        if elem > largest_number:  # change the value if new number is larger
            largest_number = elem
    return largest_number


def is_equal(list: list[int], list2: list[int]) -> bool:
    """Given is_equal, return a bool based on if the lists are equal to each other."""
    if len(list) != len(list2):
        return False
    list_idx: int = 0
    while list_idx < len(list):  # while loop for list
        for elem in list2:  # for in for list 2
            if elem != list[list_idx]:  # if the numbers from list and list2 are unequal
                return False
            list_idx += 1
    return True


def extend(list: list[int], list2: list[int]) -> None:
    """Given extend, return nothing append list 2 to the end of list."""
    for elem in list2:
        list.append(elem)