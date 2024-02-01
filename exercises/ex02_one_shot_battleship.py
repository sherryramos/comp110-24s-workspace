"""One shot battleship!"""
__author__ = 730711248

GRID: int = 4
SECRET_ROW: int = 3
SECRET_COLUMN: int = 2

invalid_row: bool = False
invalid_column: bool = False

guess_row: int = int(input(f"Guess a row: "))
if not(1 <= guess_row <= GRID):
    invalid_row: bool = True

#if user row guess is too high/low allow user to guess again until valid
while invalid_row:
    if not(1 <= guess_row <= GRID):
        new_row: int = int(input(f"The grid is only {GRID} by {GRID}. Try again: "))
    if 1 <= new_row <= GRID: 
        invalid_row = False
        guess_row = new_row

guess_column: int = int(input(f"Guess a column: "))
if not(1 <= guess_column <= GRID):
    invalid_column: bool = True

#if user column guess is too high/low allow user to guess again until valid
while invalid_column:
    if not(1 <= guess_column < GRID):
        new_column: int = int(input(f"The grid is only {GRID} by {GRID}. Try again: "))
    if 1 <= new_column <= GRID: 
        invalid_column = False
        guess_column = new_column

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

#if guess is hit (red box) or miss (white box)
result: str = WHITE_BOX
if guess_row == SECRET_ROW and guess_column == SECRET_COLUMN:
    result = RED_BOX

#printing the boxes
row_indx: int = 1
while row_indx <= GRID: #row while loop
    emojis: str =""
    column_indx: int = 1
    if guess_row == row_indx: 
        while column_indx <= GRID: #column while loop
            if guess_column == column_indx:
                emojis = emojis + result
            else:
                emojis = emojis + BLUE_BOX
            column_indx += 1
    else: 
        while column_indx <= GRID:
            emojis = emojis + BLUE_BOX
            column_indx += 1
    print(emojis)
    row_indx += 1

#if user guess is correct
if guess_row == SECRET_ROW and guess_column == SECRET_COLUMN:
    print(f"Hit!")
    #user row guess is correct
elif guess_row == SECRET_ROW and guess_column != SECRET_COLUMN:
    print(f"Close! Correct row, wrong column.")
    #user column guess is correct
elif guess_row != SECRET_ROW and guess_column == SECRET_COLUMN:
    print(f"Close! Correct column, wrong row.")
else:
    print(f"Miss!")