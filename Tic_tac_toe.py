import random
board = [' ' for _ in range(9)]
players = ['X', 'O']
player = random.choice(players)
print("Welcome to Tic-Tac-Toe Game!!")
print('  ' + ' ----------- ')
print(f"It's {player}'s turn ")


def print_board():
    print(' ')
    print(board[0] + ' | ' + board[1]  + ' | ' + board[2])
    print('' + '-' + ' ' + '' + '-' + ' ' + '-' + ' ' + '-' + ' - ')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('' + '-' + ' ' + '' + '-' + ' ' +'-' + ' ' + '-' + ' - ')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
    print(' ')

def check_move():
    if ' ' in board:
        return True
    else:
        return False

def make_move():
    board[board_number] = player

def check_win():
    if board[0]==board[4]==board[8]=='X' or board[0]==board[1]==board[2]=='X' \
        or board[0]==board[3]==board[6]=='X' or board[2]==board[4]==board[6]=='X' \
        or board[1]==board[4]==board[7]=='X' or board[2]==board[5]==board[8] == 'X'\
        or board[6]==board[7]==board[8]=='X' or board[3]==board[4]==board[5] == 'X'\
        or board[6]==board[7]==board[8]=='O' or board[3]==board[4]==board[5] == 'O'\
        or board[0]==board[4]==board[8]=='O' or board[0]==board[1]==board[2]=='O' \
        or board[0]==board[3]==board[6]=='O' or board[2]==board[4]==board[6]=='O' \
        or board[1]==board[4]==board[7]=='O' or board[2]==board[5]==board[8] == 'O':
        return True
    else:
        return False
            

while True:
    print_board()
    board_number = int(input('Pick a number to place the move(0-8): '))

    if player == 'X':
        if check_move():
            if board[board_number] == ' ':
                make_move()
                if check_win():
                    print_board()
                    print('X Won the match!! ')
                    break
                else:
                    player = 'O'
                    print(f"It's {player}'s turn")
                    continue
            else:
                print('Already occupied! Choose again')
                continue
        else:
            print("It's a tie!! ")
            break

    if player == 'O':
        if check_move():
            if board[board_number] == ' ':
                make_move()
                if check_win():
                    print_board()
                    print('O won the match!! ')
                    break
                else:
                    player = 'X'
                    print(f"It's {player}'s turn")
                    continue
            else:
                print("Already occupied! Choose again")
                continue
        else:
            print("It's a tie!! ")
            break
