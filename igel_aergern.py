""""
Author: Gaku Iwata

I affirm that I have carried out my academic endeavors
with full academic honesty. Gaku Iwata
"""
import igel_view as view
import random

PLAYER_COUNT = 4
COLORS = ['Y', 'R', 'G', 'P', 'B', 'O']

def run_game():
    """
    Run one full game of Igel Aergern.
    """
    # *** Do NOT modify this function ***
    players = create_players(PLAYER_COUNT)
    board = create_board()
    update_interface(board)
    start_up_phase(board, players)
    main_phase(board, players)

def create_players(num):
    """
    Create list of num players.
    

    Parameters
    -----
    num: int
        Number of players.

    Returns
    -----
    list
        List of player colors.
    """
    return COLORS[:num]

def create_board():
    """
    Ceate and return an empty board.
    

    Returns
    -----
    list
        a 6*9 game board.
    """
    return [["" for _ in range(9)] for _ in range(6)]

def board_to_string(board):
    """
    Converting the list into string.
    Each cell in the board is separated by a '|' character. Each row of the board is separated by a '//' sequence. 

    
    Parameters
    -----
    board: list 
        Game board.

    Returns
    -----
    str
        String representation of game board.
    """
    board_str = ""
    for row in board:
        row_str = ""
        for cell in row:
            if cell:  # If the cell is not empty
                row_str += cell
            row_str += "|"  # Add cell separator after each cell
        board_str += row_str[:-1] + "//" # Remove the last cell separator for adding row separator and add row separator
    return board_str[:-2]  # remove the last "//"

def update_interface(board):
    """
    Update the terminal display of the board.
    

    Parameter
    -----
    board: list
        Game board.
    """
    board_str = board_to_string(board)
    view.refresh_view(board_str)

def start_up_phase(board, players):
    """
    Run the start up phase where players place their tokens on the board.
    

    Parameters
    ------
    board: list
        Game board.
    players: list
        List of players.
    """
    for hedgehog_number in range(1,5):
        for player in players:
            place_hedgehog(player,hedgehog_number,board)

def place_hedgehog(player,hedgehog_number,board):
    """
    Place a hedgehog on game board

    
    Parameters
    ------
    player: str
        The player who is playing the hedgehog.
    hedgehog_number: int
        Hedgehog identifier.
    board: list
        Game board. 
    """
    print(f"Player {player} places hedgehog no {hedgehog_number}")
    user_input = input(f"Player {player}, in which row do you want to place your hedgehog? ")
    row = int(user_input)
    board[row - 1][0] += player
    update_interface(board)

def main_phase(board, players):
    """
    Run the main phase of the game.
     
    Players roll the die, optionally move one of their tokens sideways, and move
    a token forward. This phase ends when one player has won.

    
    Parameters
    -----
    board: list
        Game board.
    players: list
        List of players.
    """ 
    while not winning(board,players):
        for player in players:
            player_turn(player,board)
    pass

def winning(board,players):
    """
    Check if any player has won

    
    Parameters
    -----
    board: list
        Game board.
    players: list
        List of players

    Returns
    -----
    Bool: True if there is a winner, False otherwise
    """
    sum_column = ""
    
    for i in range(0,6):
        sum_column += board[i][8]

    num_char = len(sum_column)
    count = 0
    for char in range(num_char):
        for player in players:
            if sum_column[char] == player:
                count += 1
    if count >= 3:
        return True
    else:
        return False

def player_turn(player,board):
    """
    Perform a player's turn

    Parameters
    -----
    player: str
        The current player.
    board: list
        Game board
    """
    print(f"Player {player}'s turn")
    die_roll = roll_die() 
    print(f"Die roll: {die_roll}")
    sidestep(board,player) 
    forward(board,player,die_roll) 
    update_interface(board)

def roll_die():
    """
    Roll a six-sided die

    Return
    -----
    int
        A random number between 1 and 6
    """
    return random.randint(1, 6)
    
def sidestep(board, player):
    """
    Slide a hedgehog token sideways

    Parameters
    -----
    board: list
        Game board.
    player: str
        The current player.
    """
    print("Do you want to slide a hedgehog token sideways?")
    row_slide = int(input("Input 0 to pass or the row number for the token you want to slide")) - 1 
    if row_slide != -1:
        column_slide = int(input("Now input the column number for the token you want to slide")) - 1
        board[row_slide][column_slide] = board[row_slide][column_slide][:-1] #eliminate the last letter of the element

        print("Do you want to slide this hedgehog up or down?")
        up_or_down_slide = input("Choose U or D")
        
        if up_or_down_slide == "U":
            board[row_slide - 1][column_slide] += player # add new elements
        elif up_or_down_slide == "D":
            board[row_slide + 1][column_slide] += player
    update_interface(board)

def forward(board, player, die_roll):
    """
    Move a hedgehog token forward

    Parameters
    -----
    board: list
        Game board.
    player: str
        The current player.
    die_roll: int
        The result of rolling a die.
    """
    print(f"Player {player}'s turn")
    print(f"Die roll: {die_roll}")
    print(f"Which hedgehog from row {die_roll} do you want to move forward?")
    column_forward = int(input("Input the column number for the token you want to move forward")) - 1
    board[die_roll-1][column_forward +1] += board[die_roll-1][column_forward][-1] # add new element
    board[die_roll-1][column_forward] = board[die_roll-1][column_forward][:-1] #eliminate the last letter of the element
  
############
### Main ###

if __name__=='__main__':
    run_game()


