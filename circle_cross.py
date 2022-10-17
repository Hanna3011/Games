import random
import numpy as np


def circle_and_cross_board():
    board = np.array(
        ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    )
    board = board.reshape(3, 3)
    print(board)
    return board


def who_starts():
    first_player = ""
    while first_player != "computer" and first_player != "me":
        first_player = input(
            "choose the first player (computer/me): "
        )
    return first_player


def rename_coordinates(board):
    a1 = board[0, 0]
    a2 = board[0, 1]
    a3 = board[0, 2]
    a4 = board[1, 0]
    a5 = board[1, 1]
    a6 = board[1, 2]
    a7 = board[2, 0]
    a8 = board[2, 1]
    a9 = board[2, 2]
    return a1, a2, a3, a4, a5, a6, a7, a8, a9


def if_win(a1, a2, a3, a4, a5, a6, a7, a8, a9):
    if (
            (a1 == a2 and a2 == a3) or
            (a4 == a5 and a5 == a6) or
            (a7 == a8 and a8 == a9) or
            (a1 == a4 and a4 == a7) or
            (a2 == a5 and a5 == a8) or
            (a3 == a6 and a6 == a9) or
            (a1 == a5 and a5 == a9) or
            (a7 == a5 and a5 == a3)
    ):
        win = True
    else:
        win = False
    return win


def if_dead_heat(a1, a2, a3, a4, a5, a6, a7, a8, a9, win):
    if (
            a1 != "1" and
            a2 != "2" and
            a3 != "3" and
            a4 != "4" and
            a5 != "5" and
            a6 != "6" and
            a7 != "7" and
            a8 != "8" and
            a9 != "9" and
            win == False
    ):
        dead_heat = True
    else:
        dead_heat = False
    return dead_heat


def put_sign_to_board(board, move: int, sign: str, computer_move):
    x = (move-1)//3
    y = (move+2) % 3
    if board[x, y] == str(move):
        board[x, y] = sign
        possible_of_move = True
    else:
        possible_of_move = False
        if computer_move == False:
            print("This place is busy")
    return board, possible_of_move


def result(board, player):
    actual_situation = rename_coordinates(board)
    a1 = actual_situation[0]
    a2 = actual_situation[1]
    a3 = actual_situation[2]
    a4 = actual_situation[3]
    a5 = actual_situation[4]
    a6 = actual_situation[5]
    a7 = actual_situation[6]
    a8 = actual_situation[7]
    a9 = actual_situation[8]
    win = if_win(a1, a2, a3, a4, a5, a6, a7, a8, a9)
    dead_heat = if_dead_heat(
        a1, a2, a3, a4, a5, a6, a7, a8, a9, win
    )
    if win == True and player == "computer":
        print("computer won")
        current_result = True
    elif win == True and player == "you":
        print("you won!")
        current_result = True
    elif dead_heat == True:
        print("nobody won")
        current_result = True
    else:
        current_result = False
    return current_result


def near_win_computer_move(a1, a2, a3, a4, a5, a6, a7, a8, a9):
    computer_move = None
    win_lines = (
        (a1, a2, a3),
        (a4, a5, a6),
        (a7, a8, a9),
        (a1, a4, a7),
        (a2, a5, a8),
        (a3, a6, a9),
        (a3, a5, a7),
        (a1, a5, a9)
    )
    for line in win_lines:
        x = line[0]
        y = line[1]
        z = line[2]
        if x == y and z != "o" and z != "x":
            computer_move = int(z)
            break
        elif x == z and y != "o" and y != "x":
            computer_move = int(y)
            break
        elif y == z and x != "o" and x != "x":
            computer_move = int(x)
            break
    return computer_move


def non_lose_computer_move(a5, your_sign, number_of_move):
    computer_move = None
    if a5 == your_sign and number_of_move == 2:
        computer_move = random.choice([1, 3, 7, 9])
    return computer_move


def signs():
    your_sign = ""
    while your_sign != "o" and your_sign != "x":
        your_sign = input("choose your sign (x/o): ")
    if your_sign == "x":
        computer_sign = "o"
    elif your_sign == "o":
        computer_sign = "x"
    return your_sign, computer_sign


def computer_moves(
        board, computer_sign, level, first_move,
        number_of_move, your_sign, computer_turn
):
    actual_situation = rename_coordinates(board)
    a1 = actual_situation[0]
    a2 = actual_situation[1]
    a3 = actual_situation[2]
    a4 = actual_situation[3]
    a5 = actual_situation[4]
    a6 = actual_situation[5]
    a7 = actual_situation[6]
    a8 = actual_situation[7]
    a9 = actual_situation[8]
    computer_move = None
    possible_of_move = False
    while possible_of_move != True:
        if level == "easy":
            computer_move = random.randint(1, 9)
        elif level == "medium":
            if first_move == True:
                computer_action = computer_first_move()
                computer_move = computer_action[0]
                first_move = computer_action[1]
            elif a5 == '5':
                computer_move = 5
            else:
                computer_move = near_win_computer_move(
                    a1, a2, a3, a4, a5, a6, a7, a8, a9
                )
                if computer_move == None:
                    computer_move = random.randint(1, 9)
        elif level == "hard":
            if first_move == True:
                computer_action = computer_first_move()
                computer_move = computer_action[0]
                first_move = computer_action[1]
            elif a5 == '5':
                computer_move = 5
            else:
                computer_move = near_win_computer_move(
                    a1, a2, a3, a4, a5, a6, a7, a8, a9
                )
                if computer_move == None:
                    computer_move = computer_way_to_win(
                        a1, a2, a3, a4, a5, a6, a7, a8, a9,
                        number_of_move, computer_sign, your_sign
                    )
                    if computer_move == None:
                        computer_move = non_lose_computer_move(
                            a5, your_sign, number_of_move
                        )
                        if computer_move == None:
                            computer_move = random.randint(1, 9)
        putting = put_sign_to_board(
            board, computer_move, computer_sign, computer_turn
        )
        possible_of_move = putting[1]
    print("computer picked place: ", computer_move)
    board = putting[0]
    print(board)
    return board, first_move


def computer_way_to_win(
        a1, a2, a3, a4, a5, a6, a7, a8, a9,
        number_of_move, computer_sign, your_sign
):
    if (
            number_of_move == 3 and
            a5 == computer_sign and
            a2 == your_sign
    ):
        computer_move = 1
    elif (
            number_of_move == 3 and
            a5 == computer_sign and
            a4 == your_sign
    ):
        computer_move = 7
    elif (
            number_of_move == 3 and
            a5 == computer_sign and
            a6 == your_sign
    ):
        computer_move = 3
    elif (
            number_of_move == 3 and
            a5 == computer_sign and
            a8 == your_sign
    ):
        computer_move = 9
    elif (
            number_of_move == 5 and
            a5 == computer_sign and
            a2 == your_sign and
            a1 == computer_sign and
            a9 == your_sign
    ):
        computer_move = 7
    elif (
            number_of_move == 5 and
            a5 == computer_sign and
            a4 == your_sign and
            a7 == computer_sign and
            a3 == your_sign
    ):
        computer_move = 9
    elif (
            number_of_move == 5 and
            a5 == computer_sign and
            a6 == your_sign and
            a3 == computer_sign and
            a7 == your_sign
    ):
        computer_move = 1
    elif (
            number_of_move == 5 and
            a5 == computer_sign and
            a8 == your_sign and
            a9 == computer_sign and
            a1 == your_sign
    ):
        computer_move = 3
    else:
        computer_move = None
    return computer_move


def computer_first_move():
    computer_move = 5
    first_move = False
    return computer_move, first_move


def your_moves(board, your_sign, computer_turn):
    possible_of_move = False
    your_move = ""
    while possible_of_move == False:
        your_move = input("which place you picked? ")
        while your_move not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            try:
                your_move = int(your_move)
            except:
                your_move = input("which place you picked? ")
            if your_move not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                print("Na planszy nie ma takiego pola")
            else:
                putting = put_sign_to_board(
                    board, your_move, your_sign, computer_turn
                )
                possible_of_move = putting[1]
    board = putting[0]
    print(board)
    return board


def game():
    board = circle_and_cross_board()
    first_player = who_starts()
    your_sign, computer_sign = signs()
    level = ""
    while level != "easy" and level != "medium" and level != "hard":
        level = input("pick the level (easy, medium, hard): ")
    number_of_move = 1
    if first_player == "computer":
        computer_turn = True
        first_move = True
    else:
        computer_turn = False
        first_move = False
    while True:
        if computer_turn:
            computer_action = computer_moves(
                board, computer_sign, level, first_move,
                number_of_move, your_sign, computer_turn
            )
            board, first_move = computer_action
            current_result = result(board, first_player)
        else:
            board = your_moves(board, your_sign, computer_turn)
            current_result = result(board, "you")
        computer_turn = not computer_turn
        number_of_move += 1
        if current_result:
            print("Game is finished")
            break


if __name__ == "__main__":
    game()
