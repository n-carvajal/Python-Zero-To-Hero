"""02 - Tic Tac Toe (VS CPU)"""

# Imports
from random import randint


# Functions
def board_view():
    """
    Prints a formatted version of 'board'.
    """
    print("  0   1   2")
    print(f"0 {row1[0]} | {row1[1]} | {row1[2]}")
    print(f"1 {row2[0]} | {row2[1]} | {row2[2]}")
    print(f"2 {row3[0]} | {row3[1]} | {row3[2]}")


def horizontal_check(symbol):
    """
    Checks if either player or cpu have won horizontally.

    Returns win.
    """
    for i in board:
        if i == [symbol, symbol, symbol]:
            return "win"


def vertical_check(symbol):
    """
    Checks if player or cpu have won vertically.

    Returns win.
    """
    for i in range(3):
        if row1[i] == symbol and row2[i] == symbol and row3[i] == symbol:
            return "win"


def diagonal_check_1(symbol):
    """
    Checks if either player or cpu have won diagonally L-R.

    Returns win.
    """
    if row1[0] == symbol and row2[1] == symbol and row3[2] == symbol:
        return "win"


def diagonal_check_2(symbol):
    """
    Checks if either player or cpu have won diagonally R-L.

    Returns win.
    """
    if row1[2] == symbol and row2[1] == symbol and row3[0] == symbol:
        return "win"


def draw_check():
    """
    Checks if no empty spaces on board.

    Returns draw.
    """
    if "■" not in row1 and "■" not in row2 and "■" not in row3:
        return "draw"


def check_win(symbol):
    """
    Combines the vertical, horizontal and diagonal functions into one.
    """
    if (
        horizontal_check(symbol)
        or vertical_check(symbol)
        or diagonal_check_1(symbol)
        or diagonal_check_2(symbol) == "win"
    ):
        return "win"


# Variables
row1 = ["■", "■", "■"]
row2 = ["■", "■", "■"]
row3 = ["■", "■", "■"]
board = [row1, row2, row3]

name = input("Welcome, what is your name: ")
print(f"\nWelcome to Tic Tac Toe, {name}")
print(
    "The aim of the game is for you to make a straight line of 'X's across a "
    "3x3 board."
)
print("\nDo you want to play?")
game_on = True
while game_on:
    play_on = input("Type 'Yes' or 'No': ").lower()
    if play_on == "yes":
        print(f"\nSmart choice {name}, let's go...")
        print(
            "\nThe game board is comprised of 3 rows (0,1,2) and 3 columns "
            "(0,1,2).\n"
        )
        board_view()
        print(
            "\nWhen asked for a row, enter a 0, 1, or a 2 to select it.\n"
            "Then when asked for a column enter a 0, 1 or a 2 to select it."
        )
        break
    elif play_on == "no":
        print(f"\nSorry to hear you are so boring {name}.")
        print("Good bye.")
        playing = False
        break
    else:
        print(f"\nThat's an invalid input {name}, learn to type.")
        print("Try again.")
        continue
playing = True
while playing:
    # Player choice
    player_choice = True
    while player_choice:
        player_row_str = input("\nPlease choose your row: ")
        player_column_str = input("Please choose your column: ")
        if not player_row_str.isdigit() or not player_column_str.isdigit():
            print("That input is invalid.  Please enter a number 0 - 2.")
            print("Try again.")
            continue
        player_row = int(player_row_str)
        player_column = int(player_column_str)
        if (
            player_row < 0
            or player_row > 2
            or player_column < 0
            or player_column > 2
        ):
            print("That input is invalid.  Please enter a number 0 - 2.")
            print("Try again.")
        elif board[player_row][player_column] == "■":
            board[player_row][player_column] = "X"
            break
        else:
            print("Position Taken.")
            continue
    print(f"You chose row {player_row}, column {player_column}")
    board_view()
    if check_win("X") == "win":
        print(f"You win {name}!")
        playing = False
        break
    elif draw_check() == "draw":
        print("It's a draw.")
        playing = False
        break
    # CPU Choice
    cpu_choice = True
    while cpu_choice:
        cpu_row = randint(0, 2)
        cpu_column = randint(0, 2)
        if board[cpu_row][cpu_column] == "■":
            board[cpu_row][cpu_column] = "O"
            print(f"I chose row {cpu_row}, column {cpu_column}")
            break
        else:
            continue
    board_view()
    if check_win("O") == "win":
        print("I win.")
        playing = False
        break
    elif draw_check() == "draw":
        print("It's a draw.")
        playing = False
        break
print("Game Over")
