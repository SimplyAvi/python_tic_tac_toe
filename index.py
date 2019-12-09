# print('hello world')

# from IPython.display import clear_output

# Write a function that can print out a board. 
# Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, 
# so you get a 3 by 3 board representation.
import random
def display_board(board):
    # clear_output()  # dont use in vscode
#   print('\n'*100) #use in vscode
    print(board[7] + '|'+board[8]+'|'+board[9])
    print('-|-|-')
    print(board[4] + '|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[1] + '|'+board[2]+'|'+board[3])

#  Write a function that can take in a player input and assign their marker as 'X' or 'O'.
#  Think about using while loops to continually ask until you get a correct answer.


def player_input():
    player_choice_marker = ''

    while not(player_choice_marker == "X" or player_choice_marker == "O"):
        player_choice_marker = input(
            'Player 1: Do you choose to be X or O? ').upper()
        if player_choice_marker == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')
#   returns a list of assigned X,O to the players choice so that you can refer to player 1 as 0, player 2 as 1

#  Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired 
# position (number 1-9) and assigns it to the board.

def place_marker(board, marker, position):
    board[position] = marker
# places the maker on the tic tak toe board


# Write a function that takes in a board and a mark(X or O) and then checks to see if that mark has won
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal
# all win conditions for the board

# Write a function that uses the random module to randomly decide which player goes first. 
# You may want to lookup random.randint() Return a string of which player went first.

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
# randomly choosing which player starts the game first

#  Write a function that returns a boolean indicating whether a space on the board is freely available.


def space_check(board, position):

    return board[position] == ' '
# placing a space for the X and O's onto the board

