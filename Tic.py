# Welcome message
# Choose either X or O
# Display board
# Randomly pick who goes first
# Player 1 puts marker on board
    # Check if valid position -> (Position valid or taken?)
# Check if win
# Check if tie
# Display board
# Player 2 puts marker on board
    # Check if valid position -> (Position valid or taken?)
# Check if win
# Check if tie
# If win, display message (ex. Player 1 wins!)
# Ask to replay
# If tie, display message (ex. Tie game!)
# Ask to replay
#['#','','O','X','O','X','O','O','X','O']

import random


def board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def select_player_marker(player_1_marker,player_2_marker):
    player_1_marker = ''
    player_2_marker = ''
    while player_1_marker !='X' and player_1_marker !='O':
        player_1_marker = input('Player 1: Please select X or O ').upper()

    if player_1_marker == 'X':
        player_2_marker = 'O'
    else:
        player_2_marker = 'X'

    return(player_1_marker,player_2_marker)


def pick_first_player():
    if random.randint(1,2) == 1:
        return ('Player 1')
    else:
        return ('Player 2')


def check_win(board):
    return (board[1] == board[2] == board[3] and board[1:4] != ['']*3 or
            board[4] == board[5] == board[6] and board[4:7] != ['']*3 or
            board[7] == board[8] == board[9] and board[7:10] != ['']*3 or
            board[1] == board[4] == board[7] and board[1:8:3] != ['']*3 or
            board[2] == board[5] == board[8] and board[2:9:3] != ['']*3 or
            board[3] == board[6] == board[9] and board[3:10:3] != ['']*3 or
            board[1] == board[5] == board[9] and board[1:10:4] != ['']*3 or
            board[3] == board[5] == board[7] and board[3:8:2] != ['']*3 )


def check_tie(board):
    return check_win(board) == False and board.count('') == 0


def check_space_taken(board,position):
    return board[position] == ''


def place_marker(board,marker,position=None):
    position = int(input('Please select a position 1-9: '))
    while position not in range(1,10) or check_space_taken(board,position) == False:
        position = int(input('Invalid entry, Try again: '))
    board[position] = marker


def replay():
    return input('Do you want to play again? Enter Y or N: ').lower().startswith('y')


play_game = True

player_1_marker = ''
player_2_marker = ''


while play_game:
    play_board = ['#', '', '', '', '', '', '', '', '', '']
    print('Welcome to Tic Tac Toe!')
    player_1_marker,player_2_marker = select_player_marker(player_1_marker,player_2_marker)
    print('\n')
    turn = pick_first_player()
    print(turn+' will go to first!')

    game_play = True
    while game_play:
        if turn == 'Player 1':
            board(play_board)
            print('Player 1 ')
            place_marker(play_board,player_1_marker)
            board(play_board)
            if check_win(play_board):
                print('Player 1 wins!')
                game_play = False
                play_game = False
            if check_tie(play_board):
                print('Tie game!')
                game_play = False
                play_game = False
            turn = 'Player 2'
        else:
            board(play_board)
            print('Player 2 ')
            place_marker(play_board,player_2_marker)
            board(play_board)
            if check_win(play_board):
                print('Player 2 wins!')
                game_play = False
                play_game = False
            if check_tie(play_board):
                print('Tie game!')
                game_play = False
                play_game = False
            turn = 'Player 1'
    if replay():
        play_game = True
        game_play = True








