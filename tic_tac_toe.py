def display_board(board):
    # global board
    for i in board:
        print i
    # print board

# display_board()

def player_input():
    sign_1 = 'x'
    sign_2 = 'o'
    player_1 = input(str("please enter your name as 1st player : "))
    player_2 = input(str("please enter your name as 2nd player: "))
    print ("1st player has sign : %s" %sign_1)
    print ("2nd player has sign : %s" %sign_2)

# player_input()

def valid_input(place, s):
    return place in range(1, 10) and place not in s

def winner(board):
    combinations = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)]
        ]
    for k in combinations:
        i1, j1 = k[0]
        i2, j2 = k[1]
        i3, j3 = k[2]
        try:
            if board[i1][j1] == board[i2][j2] and board[i2][j2] == board[i3][j3]:

                print board[i1][j1] + ' is the winner'
                return True
        except:
            print i1, j1, i2, j2, i3, j3
        # a, b, c = k[0], k[1], k[2]
    return False


def logic():
    # global board
    board = [[1,2,3], [4,5,6], [7,8,9]]
    count = 0
    turn = 1
    s = set()
    flag = False
    while not flag and count < 9:
        display_board(board)
        if turn == 1:
            place = int(input("PLAYER-1 where do you want to place your x : "))
            if valid_input(place, s):
                for r in board:
                    for c,d in enumerate(r):
                        if d == place:
                            r[c] = 'x'
                turn = 2
                count += 1
                s.add(place)
        else:
            place = int(input("PLAYER 2 where do you want to place your o : "))
            if valid_input(place, s):
                for r in board:
                    for c,d in enumerate(r):
                        if d == place:
                            r[c] = 'o'
                turn = 1
                count += 1
                s.add(place)
        flag = winner(board)
    else:
        if not flag:
            
            print ("draw")
    display_board(board)


logic()
# def place_marker():
#     marker_tracker = []
#     def one():
#         player_1_turn = int(input("where do you want to place your x : "))
#
#         for i in board:
#             if player_1_turn not in marker_tracker:
#                 marker_tracker.append(player_1_turn)
#                 for j,k in enumerate(i):
#                     if k == player_1_turn:
#                         print board
#                         i[j] = "x"
#                         print board
#
#
#
#     one()
#     def two():
#         player_2_turn = int(input("where do you want to place your o : "))
#         for a in board:
#             if player_2_turn not in marker_tracker:
#                 marker_tracker.append(player_2_turn)
#                 for b,c in enumerate(a):
#                     if c == player_2_turn:
#                         print board
#                         a[b] = "o"
#                         print board
#                         return
#
#             else:
#                 continue
#     two()
#place_marker()
