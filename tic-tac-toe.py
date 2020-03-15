from IPython.display import clear_output
def display_board(board):
    clear_output()
    print('   |   | ')
    print(' '+ board[7] + ' | ' + board[8] + ' | '+ board[9])
    print('   |   | ')
    print('------------')
    print(' '+ board[4] + ' | ' + board[5] + ' | '+ board[6]) 
    print('   |   | ')
    print('------------')
    print(' '+ board[1] + ' | ' + board[2] + ' | '+ board[3])
    print('   |   | ')

def player_input():
    '''Output=(player1_marker,player2_marker)'''
    marker=''
    while marker!='X' and marker!='O':
        marker=input("Player1:Choose X or O: ").upper()
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board,marker,position):
    board[position]=marker

def win_check(board,mark):
    #this checks the row
       return ((board[1]==mark and board[2]==mark and board[3]==mark) or
               (board[4]==mark and board[5]==mark and board[6]==mark) or
               (board[7]==mark and board[8]==mark and board[9]==mark) or
    #this check the column
               (board[7]==mark and board[4]==mark and board[1]==mark) or
               (board[8]==mark and board[5]==mark and board[2]==mark) or
               (board[9]==mark and board[6]==mark and board[3]==mark) or
    #this will check the daigonal
               (board[7]==mark and board[5]==mark and board[3]==mark) or
               (board[9]==mark and board[5]==mark and board[1]==mark))

import random
def choose_first():
    flip=random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board,position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    #Board Is full if we return true
    return True

def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        return int(input('Choose a position:(1-9) '))
    return position

def replay():
    choice=input('Play Again? Enter Yes or No')
    return choice=='Yes'

#while loop to keep running the game
print("WELCOME TO TIC-TAC-TOE")
while True:
    #set everything like board,who first,choice marker
    the_board=[' ']*10
    player1_marker,player2_marker=player_input()
    turn = choose_first()
    print(turn + 'will go first!!!')
    play_game=input('Ready to play game? Y or N')
    if play_game=='Y':
        game_on = True
    else:
        game_on = False
    #game play
    while game_on:
        if turn== 'Player 1':
                display_board(the_board)
                position = player_choice(the_board)
                place_marker(the_board,player1_marker,position)
                if win_check(the_board,player1_marker):
                    display_board(the_board)
                    print('Player 1 has won the game!!!')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print("TIE GAME!!")
                        game_on = False
                    else:
                        turn = 'Player 2'
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player2_marker,position)
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player 2 has won the game!!!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!!!")
                    game_on = False
                else:
                    turn ='Player 1'
    if not replay():
        break
#break out of while loop on replay()
