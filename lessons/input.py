"""Practice with User Input"""

numbers: str = "211822"
current: int = 0
number_evens: int = 0

while current < 6:
    num: int = int(numbers[current])
    if num % 2 == 0:
        number_evens = number_evens + 1
    current = current + 1
print(number_evens)


#why does num have to be inside the while instead of with the other variables???