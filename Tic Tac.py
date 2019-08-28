import random
def display_board(board):
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(' |'+' |')
    print('-' + '-' + '-' + '-' + '-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(' |' + ' |')
    print('-' + '-' + '-' + '-' + '-')
    print(board[7]+'|'+board[8] +'|'+board[9])
    print(' |' + ' |')

def player_input():
    mark=''
    while not(mark=='x' or mark=='o'):
        mark=input('please select x or o')
    if mark=='x':
        return ('x','o')
    else:
        return ('o','x')

def place_mark(board,mark,position):
    board[position]=mark

def win(board,mark):
    return ((board[1] == board[2] == board[3] == mark) or (board[4] == board[5] == board[6] == mark) or (
             board[7] == board[8] == board[9] == mark) or
             (board[1] == board[5] == board[9] == mark) or (board[3] == board[5] == board[7] == mark) or
             (board[1] == board[4] == board[7] == mark) or (board[2] == board[5] == board[8] == mark) or (
              board[3] == board[6] == board[9] == mark))

def space_check(board,position):
    return (board[position]==' ')

def full_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    else:
        return True

def player_position(borad):
    position=0
    while position not in[1,2,3,4,5,6,7,8,9]and not space_check(borad,position):
        position=int(input('please select a position between 1 to 9'))
    return position

def replay():
    x=input('you wanna play agian? enter yes or no!')
    if x.lower()=='y':
        return True

def choose_first():
    p=random.randint(0,1)
    if p==0:
        return 'player1'
    else:
        return 'player2'

def main():
    print('Enjoy the TIC TAC TOE Game !')
    while True:
        the_board=[' ']*10
        display_board(the_board)
        player1_mark,player2_mark=player_input()
        turn=choose_first()
        print(turn+' will go first')
        while True:
            if turn=='player1':
                print('player1')
                position=player_position(the_board)
                place_mark(the_board,player1_mark,position)
                display_board(the_board)
                if win(the_board,player1_mark):
                    print('player1 has won the match!')
                    display_board(the_board)
                    break
                elif full_check(the_board):
                    print('GAME TIE!')
                    display_board(the_board)
                    break
                else:
                    turn='player2'
            else:
                print('player2')
                position = player_position(the_board)
                place_mark(the_board, player2_mark, position)
                display_board(the_board)
                if win(the_board, player2_mark):
                    print('player2 has won the match!')
                    display_board(the_board)
                    break
                elif full_check(the_board):
                    print('GAME TIE!')
                    display_board(the_board)
                    break
                else:
                    turn = 'player1'
        if not replay():
            break

main()