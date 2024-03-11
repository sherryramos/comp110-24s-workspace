"""Mutating functions."""
__author__ = "730711248"


def manual_append(list: list[int], integer: int) -> None:
    """Given manual_append, should mutate input and append the integer."""
    list.append(integer)
    

def double(list: list[int]) -> None:
    """Given double, ints in list should double."""
    counter: int = 0
    while counter < len(list):
        list[counter] = list[counter] * 2
        counter += 1