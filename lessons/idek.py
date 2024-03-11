def reverse(list1: list[str]) -> list[str]:
    new_list: list[str] = []
    for idx in range(0, len(list1)):
        new_list.append(list1[len(list1) - idx])
    return new_list

lists: list[str] = ["apple", "ball", "cat"]
reverse(lists)
# from lessons.idek import reverse
# lists: list[str] = ["apple", "ball", "cat"]