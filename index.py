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


# Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.
def full_board_check(board):

    for i in range(1, 10):
        if space_check(board, i):
            return False

    return True
# this is trickey because if you go through the itteration and put an else clause to return True if everything
# is taken the loop does not return true for the board is full!

# checks the board by calling the previous defined function
# itterates through the position to see if their all filled
# if their not all filled continue with the game, else all the positions are filled




# Write a function that asks for a player's next position (as a number 1-9) and 
# then uses the function from step 6 to check if it's a free position. If it is, 
# then return the position for later use.
def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position:(1-9) '))

    return position
#     make the input an intiger
#     not to be confused with the player_choice_marker, this is a function, not a local variable


# Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.
def replay():

    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
# asking the players if they want to play another game




# game logic with the users turns
print('Welcome to Tic Tac Toe!')

while True:
    #     Set the game
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Are you ready to play? Enter Yes or No')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == 'Player 1':
            #Player 1 Turn
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Congratulations! Player 1 has won!')
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('This game is a draw')
                    break
                else:
                    turn = 'Player 2'

        else:
            #Player2's Turn.
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Congratulations!, Player 2 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('This game is a draw')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
# game - user logic to exicute the game