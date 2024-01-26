"""A terminal interface for playing Igel Aergern.

@author: Kristina Striegnitz
@version: Winter 2024
"""

import os

# width of a cell
WIDTH = 5

def refresh_view(board_str, winner=None):
    """Prints a representation of the Igel Aergern board to the terminal.
    
    board_str -- a representation of the board as a string. The tracks/rows
    are separated from each other using // and cells within one track are
    separated using |. Empty cells are represented using an empty string.
    Otherwise they are represented as a sequence of the stacked colors. E.g.
    'RBO' represents a stack of red at the bottom, blue, and orange. 
    Here is an example of a valid board representation:
    'Y||||||||//||||||||Y//Y||R||B||O||//YR|RBO||RBOO|||||//||||||||//||BR||||||O'

    winner -- str; the name of the winner, if there is one.
    """
    os.system("cls||clear")
    board_w = board_width(board_str)
    print_header(board_w)
    print_board(board_str)
    print()
    if winner:
        display_winner(winner, board_w)

def request_input(message):
    """Requests an answer from the player and returns whatever string the player enters.
    
    message -- str; the message to display to request input from the player
    """
    answer = input(message)
    return answer.strip()

def inform(message):
    """Prints the given message to the terminal.
    
    message -- str; the message to display
    """
    print(message)

# Note: You do not need to read and understand the code that comes after this line. #

#################################
### Header and winner banners ###    

def print_header(width):
    print(center(" /~~~~~~~~~~~~~~\\", width))
    print(center(" | IGEL AERGERN |", width))
    print(center(" \\~~~~~~~~~~~~~~/", width))
    print()

def display_winner(name, width):
    message = name + " won!!"
    print()
    print(center(" ~~~ " + message + " ~~~", width))
    print()
    print()
    
############################
### Displaying the board ###

def print_board(board_str):
    rows = board_str.split("//")
    num_cols = len(rows[0].split("|"))
    print_start_goal_labels(num_cols)
    print_border(num_cols)
    for i, row in enumerate(rows):
        print_row(i+1, row)
        print_border(num_cols)
    print_col_labels(num_cols)
    
def print_row(i, row_str):
    cells = row_str.split("|")
    print("|", end="")
    for cell in cells:
        print_cell(cell)
        print("|", end="")
    print(" " + str(i), end="")
    print()

def print_cell(cell_str):
    if len(cell_str) < WIDTH:
        diff = WIDTH - len(cell_str)
        cell_str += " " * diff
    print(cell_str, end="")
    
def print_border(cols):
    print("-" * (WIDTH * cols + cols + 1))

def print_start_goal_labels(cols):
    empty_cols = cols - 2
    space = " " * (WIDTH * (empty_cols) + empty_cols) 
    print(" Start " + space + "Goal")          

def print_col_labels(cols):
    for j in range(cols):
        space = " " * (WIDTH//2)
        print(" " + space, end="") # extra blank for '|'
        print(j+1, end="")
        print(space, end="")
    print()

########################
### Helper functions ###

def board_width(board_str):
    row_str = board_str.split("//")[0]
    col_count = len(row_str.split("|"))
    board_w = WIDTH * col_count + col_count + 1 + 2
    return board_w

def center(a_string, board_w):
    diff = board_w - len(a_string)
    if diff > 0:
        pad_w = diff//2
        left_pad = " " * pad_w
        a_string = left_pad + a_string
    return a_string
    
###############
### Testing ###

# an empty board
TEST_1  = "||||||||//"
TEST_1 += "||||||||//"
TEST_1 += "||||||||//"
TEST_1 += "||||||||//"
TEST_1 += "||||||||//"
TEST_1 += "||||||||"

# some hedgehogs on the board
TEST_2  = "Y||||||||//"
TEST_2 += "||||||||Y//"
TEST_2 += "Y||R||B||O||//"
TEST_2 += "YR|RBO||RBOO|||||//"
TEST_2 += "||||||||//"
TEST_2 += "||BR||||||O"

if __name__=='__main__':
    refresh_view(TEST_1)
    print()
    print()
    input("Enter to continue ...")
    refresh_view(TEST_2)
    
