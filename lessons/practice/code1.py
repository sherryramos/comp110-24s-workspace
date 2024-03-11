def odd_and_even(list1: list[int]) -> list[int]:
    new_list: list[int] = []
    index: int = 0
    while index < len(list1):
        if list1[index] % 2 == 1 and index % 2 == 0:
            new_list.append(list1[index])
        index += 1
    return new_list

def odd_even(list1: list[int]) -> list[int]:
    new_list: list[int] = []
    for index in range(len(list1)):
        if list1[index] % 2 == 1 and index % 2 == 0:
                new_list.append(list1[index])
    return new_list