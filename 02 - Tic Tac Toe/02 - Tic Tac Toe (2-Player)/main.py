"""02 - Tic Tac Toe (2-Player)"""

# Imports
from random import randint

# Game board
row0 = ["■", "■", "■"]
row1 = ["■", "■", "■"]
row2 = ["■", "■", "■"]
board = [row0, row1, row2]


# Functions:
def show_board():
    """
    Prints a formatted version of 'board'
    """
    print("  0   1   2")
    print(f"0 {row0[0]} | {row0[1]} | {row0[2]}")
    print(f"1 {row1[0]} | {row1[1]} | {row1[2]}")
    print(f"2 {row2[0]} | {row2[1]} | {row2[2]}")


def clear_board():
    """
    Clears all inputs from board.

    By zeroing global variables row0,row1, row2 and board.
    """
    global row0
    global row1
    global row2
    global board
    row0 = ["■", "■", "■"]
    row1 = ["■", "■", "■"]
    row2 = ["■", "■", "■"]
    board = [row0, row1, row2]


def start_game():
    """
    Asks if game should start.

    Validates for 'yes' or 'no'.
    If other provides message.
    """
    game_start = False
    while not game_start:
        play_on = input("Type 'Yes' or 'No': ").lower()
        if play_on == "yes":
            print("\nGreat. Let's start.\n")
            break
        elif play_on == "no":
            print("\nOK. Bye.")
            global game_over
            game_over = True
            break
        else:
            print("You did not type 'Yes' or 'No'.")
            continue


def player_select():
    """
    Asks for input for Player 1 and Player 2.

    Assigns 'X' to P1 and 'O' to P2.
    Generates random number 0 or 1.
    Assigns 0 to P1 and 1 to P2.
    Returns first and second turn.
    """
    p1 = input("Who will be player 1: ")
    p2 = input("Who will be player 2: ")
    symbol_1 = "X"
    symbol_2 = "O"
    if randint(0, 1) == 0:
        first_turn = (p1, symbol_1)
        second_turn = (p2, symbol_2)
        return first_turn, second_turn
    else:
        first_turn = (p2, symbol_2)
        second_turn = (p1, symbol_1)
        return first_turn, second_turn


def player_choice(player, symbol):
    """
    Asks for player choice or row and column.

    Ensures input is a digit, within range 0-2, and specifies an un-taken
    position.
    """
    valid_choice = False
    while not valid_choice:
        row_string = input(f"\nPick a row {player}: ")
        column_string = input(f"Pick a column {player}: ")
        if not row_string.isdigit() or not column_string.isdigit():
            print("You did not input a numerical value.")
            continue
        row_choice = int(row_string)
        column_choice = int(column_string)
        if row_choice not in range(3) or column_choice not in range(3):
            print("You did not type a number between 0 and 2.")
            continue
        elif board[row_choice][column_choice] != "■":
            print("Position taken")
            continue
        else:
            board[row_choice][column_choice] = symbol
            break


def horizontal_check(symbol):
    """
    Checks if either player has won horizontally
    """
    for i in board:
        if i == [symbol, symbol, symbol]:
            return "win"


def vertical_check(symbol):
    """
    Checks if either player has won vertically
    """
    for i in range(3):
        if row0[i] == symbol and row1[i] == symbol and row2[i] == symbol:
            return "win"


def diagonal_check(symbol):
    """
    Checks if either player has won diagonally
    """
    if (
        row0[0] == symbol
        and row1[1] == symbol
        and row2[2] == symbol
        or row0[2] == symbol
        and row1[1] == symbol
        and row2[0] == symbol
    ):
        return "win"


def draw_check():
    """
    Checks if game is a draw
    """
    if "■" not in row0 and "■" not in row1 and "■" not in row2:
        return "draw"


def check_win(symbol):
    """
    Combines the horizontal, vertical, and diagonal win functions.
    """
    if (
        horizontal_check(symbol)
        or vertical_check(symbol)
        or diagonal_check(symbol) == "win"
    ):
        return "win"


def replay_game():
    """
    Asks if players want to replay.

    Validates answer is either 'yes' or 'no'.
    """
    game_replay = False
    print("\nWould you like to play again?")
    while not game_replay:
        replay = input("Type 'Yes' or 'No': ").lower()
        if replay == "yes":
            return True
        elif replay == "no":
            return False
        else:
            print("You did not type 'Yes' or 'No'.")
            continue


# Game:
print("Welcome to Tic Tac Toe")
print("Would you like to play?\n")
start_game()
game_over = False
while not game_over:
    (player1, p1symbol), (player2, p2symbol) = player_select()
    show_board()
    print("The board is empty.\n")
    game_won = False
    while not game_won:
        player_choice(player1, p1symbol)
        show_board()
        if check_win(p1symbol) == "win":
            print(f"{player1} wins with {p1symbol}")
            if replay_game():
                clear_board()
                show_board()
                continue
            else:
                game_over = True
                break
        elif draw_check() == "draw":
            print("It's a draw!")
            if replay_game():
                clear_board()
                show_board()
                continue
            else:
                game_over = True
                break
        player_choice(player2, p2symbol)
        show_board()
        if check_win(p2symbol) == "win":
            print(f"{player1} wins with {p2symbol}")
            if replay_game():
                clear_board()
                show_board()
                continue
            else:
                game_over = True
                break
        elif draw_check() == "draw":
            print("It's a draw!")
            if replay_game():
                clear_board()
                show_board()
                continue
            else:
                game_over = True
                break
        show_board()
        print("This is the current board.")
print("Game Over")
