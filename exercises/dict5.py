"""EX05 Dictionary Utility Functions!"""
__author__ = "730711248"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    new_dict: dict[str, str] = {}
    for key in dict1:
        if dict1[key] in new_dict:
            raise KeyError
        new_dict[dict1[key]] = key
    return new_dict


def favorite_color(dict1: dict[str, str]) -> str:
    new_dict: dict[str, int] = {'color' : 0}
    fav_color_amount: int = new_dict['color']
    fav_color: str = ''
    for key in dict1:
        if dict1[key] in new_dict:
            new_dict[dict1[key]] += 1
        else:
            new_dict[dict1[key]] = 1
        if new_dict[dict1[key]] > fav_color_amount:
            fav_color_amount = new_dict[dict1[key]]
            fav_color = dict1[key]
        # elif new_dict[dict1[key]] == fav_color_amount:
            # fav_color = new_dict[] # first color in dict1
    print(new_dict)
    return fav_color


def count(list1: list[str]) -> dict[str, int]:
    dict1: dict[str, int] = {}
    for elem in list1:
        if elem in dict1:
            dict1[elem] += 1
        else:
            dict1[elem] = 1
    return dict1

def alphabetizer(list1: list[str]) -> dict[str, list[str]]:
    """Sorts list into alphabitized dictionary!"""
    dict1: dict[str, list[str]] = {}
    for elem in list1:
        word: str = elem.lower()
        if word[0] in dict1:
            dict1[word[0]] += {elem}
        else:
            dict1[word[0]] = [elem]
    return dict1


def update_attendance(dict1: dict[str, list[str]], day: str, student: str) -> None:
    if day in dict1:
        dict1[day] = dict1[day], student
    else:
        dict1[day] = student


# from exercises.dictionary import favorite_color
# favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"})
# from exercises.dictionary import count
# count(["michi", "michi", "tay", "tae", "mic", "mic", "tay", "michi", "tae", "taylor"])
# from exercises.dictionary import alphabetizer
# from exercises.dict5 import alphabetizer
# alphabetizer(["cat", "apple", "boy", "angry", "bad", "car"])
# alphabetizer(["Python", "sugar", "Turtle", "party", "table"])
# attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
# from exercises.dictionary import update_attendance
# update_attendance(attendance_log, "Tuesday" , "Vrinda")
# update_attendance(attendance_log, "Wednesday" , "Kaleb")
# print(attendance_log)
