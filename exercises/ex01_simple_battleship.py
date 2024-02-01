"""EX01 - Simple Battleship."""

__author__ = "730711248"

user_pick: str = input("Pick a secret boat location between 1 and 4: ")
user_boatlocation: int = int(user_pick)

# if input is too low or high
if user_boatlocation < 1:
    print(f"Error! {user_pick} too low!")
    exit()
if user_boatlocation > 4:
    print(f"Error! {user_pick} too high!")
    exit()

user_guess: str = input("Guess a number between 1 and 4: ")
user_guesslocation: int = int(user_guess)

# if guess is too low or high
if user_guesslocation < 1:
    print(f"Error! {user_guess} too low!")
    exit()
if user_guesslocation > 4:
    print(f"Error! {user_guess} too high!")
    exit()

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

if user_guesslocation == 1 and user_boatlocation == 1:
    print(RED_BOX + BLUE_BOX * 3)
else:
    if user_guesslocation == 1 and user_boatlocation != 1:
        print(WHITE_BOX + BLUE_BOX * 3)
    else:
        if user_guesslocation == 2 and user_boatlocation == 2:
            print(BLUE_BOX + RED_BOX + BLUE_BOX * 2)
        else:
            if user_guesslocation == 2 and user_boatlocation != 2:
                print(BLUE_BOX + WHITE_BOX + BLUE_BOX * 2)
            else:
                if user_guesslocation == 3 and user_boatlocation == 3:
                    print(BLUE_BOX * 2 + RED_BOX + BLUE_BOX)
                else:
                    if user_guesslocation == 3 and user_boatlocation != 3:
                        print(BLUE_BOX * 2 + WHITE_BOX + BLUE_BOX)
                    else:
                        if user_guesslocation == 4 and user_boatlocation == 4:
                            print(BLUE_BOX * 3 + RED_BOX)
                        else:
                            if user_guesslocation == 4 and user_boatlocation != 4:
                                print(BLUE_BOX * 3 + WHITE_BOX)

# user guess is correct
if user_boatlocation == user_guesslocation:
    print("Correct! You hit the ship.")
else:
    if user_boatlocation != user_guesslocation:
        print("Incorrect! You missed the ship.")