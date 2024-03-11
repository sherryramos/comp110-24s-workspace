"""Exercise 03 Functional Battleship!"""
__author__ = "730711248"
import random


def input_guess(grid: int, area: str) -> int:
    """Given the integer input_guess, outputs the user's guess."""
    assert area == "row" or area == "column"  # make sure rows and columns are being guessed
    guess: int = int(input(f"Guess a {area}: "))
    if not (1 <= guess <= grid):  # make sure user guess is on the grid
        while not (1 <= guess <= grid):  # allow user to reguess until guess fits the grid size
            new_guess: int = int(input(f"The grid is only {grid} by {grid}. Try again: "))
            guess = new_guess
    return guess  # return int


def print_grid(grid: int, row_guess: int, column_guess: int, correct: bool) -> None:
    """Given print_grid, creates a string of emojis, but returns nothing."""
    BLUE_BOX: str = "\U0001F7E6"
    hit: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"
    if correct:  # user guess matches secret location
        result = hit
    else:  # user guess != correct location
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


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Given correct_guess, outputs a bool representing if the user guess was correct or not."""
    if  row_guess == secret_row and column_guess == secret_column:  # user guess matches secret location
        return True
    else:  # user guess does not match secret location (incorrect guess)
        return False
    

def main(grid: int, secret_row: int, secret_column: int) -> None:
    """Given main, uses other functions to create the battleship game for user."""
    turn: int = 1  # loop counter
    while turn <= grid and correct_guess != True:
        print(f"=== Turn {turn}/5 ===")
        row_guess: int = input_guess(grid, "row")  # call input_guess for row
        column_guess: int = input_guess(grid, "column")  # call input_guess for column
        correct: bool = correct_guess(secret_row, secret_column, row_guess, column_guess)  # call correct_guess
        print_grid(grid, row_guess, column_guess, correct)
        turn += 1


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))