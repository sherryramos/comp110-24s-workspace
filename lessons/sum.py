"""Summing the elements of a list using different loops!"""
__author__ = "730711248"


def w_sum(vals: list[float]) -> float:
    """Given a list of floats, w_sum adds them together!"""
    vals_idx: int = 0
    sum: float = 0.0
    while vals_idx < len(vals):
        sum += vals[vals_idx]
        vals_idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Given a list of floats, f_sum adds them together using for loops!"""
    sum: float = 0.0
    for elem in vals:
        sum += elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Given a list of floats, f_sum adds them together using for loops and range!"""
    sum: float = 0.0
    for index in range(0, len(vals)):
        sum += vals[index]
    return sum