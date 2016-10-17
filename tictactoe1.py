import os
import random
def display_board(board):
    #os.system("clear")
    print("   |   |")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("-----------")
    print("   |   |")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("-----------")
    print("   |   |")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])

def choose_first():
    if random.randint(0,1) == 0:
        return "PLAYER-2"
    else:
        return "PLAYER-1"
# choose_first()

def player_input():
    marker = " "
    while not (marker == "X" or marker == "O"):
        marker = raw_input("PLAYER-1 : Do you want 'x' or 'O' as mark? : ").upper()
    if marker == "X":
        print("PLAYER-1 mark is 'X' & PLAYER-2 mark is 'O'")
        return ("X","O")
    else:
        print("PLAYER-1 mark is 'O' & PLAYER-2 mark is 'X'")
        return("O","X")

def place_marker(board, marker, position):
    board[position] = marker

def space_check(board,position):
    return board[position] == " "

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board, turn):
    position = " "
    while position not in "1 2 3 4 5 6 7 8 9".split() or not space_check(board, int(position)):
        position = raw_input(turn + " Choose your next position: (1-9) : ")
    return int(position)

def replay():
    return raw_input("Do you want to play again? ").lower().startswith("y")

def win(board,mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
        (board[4] == mark and board[5] == mark and board[6] == mark) or
        (board[7] == mark and board[8] == mark and board[9] == mark) or
        (board[1] == mark and board[4] == mark and board[7] == mark) or
        (board[2] == mark and board[5] == mark and board[8] == mark) or
        (board[3] == mark and board[6] == mark and board[9] == mark) or
        (board[1] == mark and board[5] == mark and board[9] == mark) or
        (board[3] == mark and board[5] == mark and board[7] == mark))

print("Welcome to Tic Tac Toe!")

while True:
    board = [" "] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print (turn + " will go first")
    game_on = True
    while game_on:
        if turn == "PLAYER-1":
            display_board(board)
            position = player_choice(board, turn)
            place_marker(board, player1_marker, position)
            if win(board, player1_marker):
                display_board(board)
                print ("Congratulation PLAYER-1! you have won the game")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("game draw")
                    break
                else:
                    turn = "PLAYER-2"
        else:
            display_board(board)
            position = player_choice(board, turn)
            place_marker(board, player2_marker, position)
            if win(board, player2_marker):
                display_board(board)
                print ("Congratulation PLAYER-2! you have won the game")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("game draw")
                    break
                else:
                    turn = "PLAYER-1"
    if not replay():
        break
