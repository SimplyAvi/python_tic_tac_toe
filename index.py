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
