"""EX05 Dictionary Utility Functions!"""
__author__ = "730711248"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, inverts the keys and values into a new dictionary!"""
    new_dict: dict[str, str] = {}
    for key in dict1:
        if dict1[key] in new_dict:  # cannot have same key
            raise KeyError
        new_dict[dict1[key]] = key 
    return new_dict


def favorite_color(dict1: dict[str, str]) -> str:
    """Given a dictionary, counts the appearences colors and returns the highest one!"""
    new_dict: dict[str, int] = {'color': 0}
    fav_color_amount: int = new_dict['color']
    fav_color: str = ''
    for key in dict1:
        if dict1[key] in new_dict:
            new_dict[dict1[key]] += 1  # apperance increase
        else:
            new_dict[dict1[key]] = 1  # first apperance
        if new_dict[dict1[key]] > fav_color_amount:  # updating fav_color to color with highest appearance
            fav_color_amount = new_dict[dict1[key]] 
            fav_color = dict1[key]
    return fav_color


def count(list1: list[str]) -> dict[str, int]:
    """Given a list, return a dictionary counting appearences!"""
    dict1: dict[str, int] = {}
    for elem in list1:
        if elem in dict1:
            dict1[elem] += 1  # appearance increase
        else:
            dict1[elem] = 1  # first appearance
    return dict1


def alphabetizer(list1: list[str]) -> dict[str, list[str]]:
    """Given a list, returns dictionary sorting list alphabetically!"""
    dict1: dict[str, list[str]] = {}
    for elem in list1:
        word: str = elem.lower()  # ensures capital and lowercase letters are the same key
        if word[0] in dict1:
            dict1[word[0]] += {elem}  # adds to existing letter key
        else:
            dict1[word[0]] = [elem]  # first appearance
    return dict1


def update_attendance(dict1: dict[str, list[str]], day: str, student: str) -> None:
    """Given a log(dict), day(str), and name(str), updates attendance!"""
    if day in dict1:  # if day is already logged
        if not (student in dict1[day]):
            dict1[day] += {student}  # adds student to day
    else:
        dict1[day] = [student]  # creates day and adds student
    return None

alphabetizer(["apple", "adam", "ball"])