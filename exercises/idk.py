BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

def game_board(row_guess: int, column_guess: int, XO) -> None:
    """Make a 3."""
    if XO == 'X':
        result = RED_BOX
    elif XO == 'O':
        result = BLUE_BOX
    row_counter: int = 1
    while row_counter <= 3:  # if row counter is above 3 value then end the loop.
        emoji_row: str = ""
        column_counter: int = 1
        if row_guess == row_counter:
            while column_counter <= 3:
                if column_guess == column_counter:
                    emoji_row += result
                else:  # column_guess != column counter.
                    emoji_row += WHITE_BOX
                column_counter += 1
        row_counter += 1
        while column_counter <= 3:
            emoji_row += WHITE_BOX
            column_counter += 1
        print(emoji_row)