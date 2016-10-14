def display(board):
    for i in board:
        print i

def player_input():
    sign_1 = 'x'
    sign_2 = 'o'
    global player_1, player_2
    player_1 = raw_input("please enter your name as player-1 : ")
    player_2 = raw_input("please enter your name as player-2: ")
    print ("%s has sign : %s" %(player_1.upper(), sign_1))
    print ("%s has sign : %s" %(player_2.upper(), sign_2))


def valid(place, s):
    return place in range(1,10) and place not in s

def win(board):
    combinations = [
                    [(0, 0), (0, 1), (0, 2)],
                    [(1, 0), (1, 1), (1, 2)],
                    [(2, 0), (2, 1), (2, 2)],
                    [(0, 0), (1, 0), (2, 0)],
                    [(0, 1), (1, 1), (2, 1)],
                    [(0, 2), (1, 2), (2, 2)],
                    [(0, 0), (1, 1), (2, 2)],
                    [(0, 2), (1, 1), (2, 0)]
                    ]
    for k in combinations:
        i0, j0 = k[0]
        i1, j1 = k[1]
        i2, j2 = k[2]
        try:
            if board[i0][j0] == board[i1][j1] == board[i2][j2]:
                display(board)
                print ("Congratulation", board[i0][j0] ,"is winner")
                return True
        except:
            print i0, j0, i1, j1, i2, j2
    return False


def main():
    board = [[1,2,3],[4,5,6],[7,8,9]]
    count = 0
    turn = 1
    s = set()
    invalid = 0
    flag = False
    player_input()
    while not flag and count < 9:
        display(board)

        if turn == 1:
            invalid += 1
            if invalid > 1:
                print ("SORRY;  ALERT : place has been already taken or it may be invalid, try again, thank you.")
            place = int(input("%s where do you want to mark x : " %player_1.upper()))
            if valid(place, s):
                for i in board:
                    for j,k in enumerate(i):
                        if k == place:
                            i[j] = "x"
                s.add(place)
                turn = 2
                count += 1
                invalid = 0

        else:
            invalid += 1
            if invalid > 1:
                print ("SORRY;  ALERT : place has been already taken or it may be invalid, try again, thank you.")
            place = int(input("%s where do you want to mark o : " %player_2.upper()))
            if valid(place, s):
                for i in board:
                    for j,k in enumerate(i):
                        if k == place:
                            i[j] = "o"
                s.add(place)
                count += 1
                turn = 1
                invalid = 0
        flag = win(board)
    else:
        if not flag:
            display(board)
            print ("game draw. Please try again")
            main()



main()
