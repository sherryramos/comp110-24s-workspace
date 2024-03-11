"""EX05 Dictionary Utility Functions - Update Attendance!"""
__author__ = "730711248"


def update_attendance(dict1: dict[str, list[str]], day: str, student: str) -> None:
    """Adds students and days to attendance dictionary!"""
    if day in dict1:
        dict1[day] = dict1[day], student
    else:
        dict1[day] = student