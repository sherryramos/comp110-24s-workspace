"""Exercise 03 Functional Battleship!"""
__author__ = "730711248"
import random

def input_guess(grid: int, area: str) -> int:
    assert area == "row" or area == "column"  # make sure rows and columns are being guessed
    guess: int = int(input(f"Guess a {area}: "))
    if not (1 <= guess <= grid):  # make sure user guess is on the grid
        while not (1 <= guess <= grid):  # allow user to reguess until guess fits the grid size
            new_guess: int = int(input(f"The grid is only {grid} by {grid}. Try again: "))
            guess = new_guess
    return guess  # return int

def print_grid(grid: int, row_guess: int, column_guess: int, correct: bool):
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"
    if correct:  # user guess matches secret location
        result = RED_BOX
    else:
        result = WHITE_BOX
    row_idx: int = 1
    while row_idx <= grid:  # while loop for rows
        box_string: str = ""
        column_idx: int = 1
        if row_guess == row_idx: 
            while column_idx <= grid:  # while loop for columns
                if column_guess == column_idx:
                    box_string += result
                else:
                    box_string += BLUE_BOX
                column_idx += 1
        else: 
            while column_idx <= grid:
                box_string += BLUE_BOX
                column_idx += 1
        print(box_string)
        row_idx += 1

def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess) -> bool:
    if secret_row == row_guess and secret_column == column_guess:  # user guess matches secret location
        return True
    else:  # user guess does not match secret location (incorrect guess)
        return False
    
def main(grid: int, secret_row: int, secret_column: int):
    turn: int = 1  # loop counter
    correct: bool = ""  # user guess match or does not match secret location
    while turn <= 5 and not(correct):
        print(f"=== Turn {turn}/5 ===")
        user_row: int = ""  # user's row guess
        user_row = input_guess(grid, "row")  # call input_guess for row
        user_column: int = ""  # user's column guess
        user_column = input_guess(grid, "column")  # call input_guess for column
        correct = correct_guess(secret_row, secret_column, user_row, user_column)  # call correct_guess
        print_grid(grid, user_row, user_column, correct)
        if correct:
            print(f"Hit!\nYou won in {turn}/5 turns!")
        elif turn < 5:  # user has not guessed correctly, but has turns left
            print("Miss!")
        else:  # all 5 turns have been used
            print("Miss!\nX/5 - Better luck next time!")
        turn += 1

if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))