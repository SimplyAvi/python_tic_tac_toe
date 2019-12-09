# print('hello world')

# from IPython.display import clear_output

# Write a function that can print out a board. 
# Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, 
# so you get a 3 by 3 board representation.
def display_board(board):
    # clear_output()  # dont use in vscode
  print('\n'*100) #use in vscode
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


