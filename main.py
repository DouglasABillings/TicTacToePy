import random


def render_board(height, width, player_moves, player_team, comp_moves, comp_team):
    """Render the game board as follows:
     123
    1###
    2###
    3###

    :param height: the height of the board
    :param width: the width of the board
    :param player_moves: a set of move tuples the player has played
    :param player_team: a character for the player's team
    :param comp_moves: a set of move tuples the enemy has played
    :param comp_team: a character for the enemy's team
    """
    # Render the first row of indexes
    index_row = " "
    for n in range(1, width + 1):
        index_row += str(n)
    print(index_row)

    # Render the game grid
    for y in range(1, width + 1):
        row = str(y)
        for x in range(1, height + 1):
            if (x, y) in player_moves:
                row += player_team
            elif (x, y) in comp_moves:
                row += comp_team
            else:
                row += '#'
        print(row)


def input_team():
    """ Get a team from the user
    :return: a character representing the user's chosen team
    """
    team_var = ''
    while team_var is not 'X' or 'O':
        team_var = input("Choose a team, X's or O's\n").upper()

        if team_var == 'X' or team_var == 'O':
            return team_var


def user_move(height, width):
    """Get a move from the user
    :param height: the height of the game board
    :param width: the width of the game board
    :return: a tuple representing the x, y coordinates of the move
    """
    x, y = 0, 0
    while x not in range(1, height + 1):
        while y not in range(1, width + 1):
            try:
                # We have to handle this in a try catch block, because it may throw an exception
                x, y = map(int, input("Please enter your move in the form of x y\n").split())
            except ValueError:
                # Make sure to handle a ValueError exception
                x, y = (0, 0)
    return x, y


def comp_move(height, width):
    """Generates a random computer move
    :param height: the height of the game board
    :param width: the width of the game board
    :return: a tuple representing the x, y coordinates of the move
    """
    a = random.randint(1, height)
    b = random.randint(1, width)
    return a, b


def game_over(player_moves, comp_moves, width, height):
    """
    Determines if the game has ended based on all the moves that have been played so far

    :param player_moves: a set of moves that the player has made
    :param comp_moves: a set of moves that the computer has made
    :param width: the width of the board
    :param height: the height of the board
    :return:
        A tuple with the following structure (Boolean, None or String)
        - The first value tells you if the game is over or not
        - The second value is None if the game isn't over or was a tie,
            otherwise it should be either "Player" or "Computer"
    """
    # Checking the Rows
    for y in range(1, height + 1):
        row_set = set()
        for x in range(1, width + 1):
            row_set.add((x, y))
        row_win = row_set.issubset(player_moves)
        if row_win is True:
            print("horizontal win")
    # Checking the Columns
    for x in range(1, width + 1):
        col_set = set()
        for y in range(1, height + 1):
            col_set.add((x, y))
        col_win = col_set.issubset(player_moves)
        if col_win is True:
            print("vertical win")
    # Checking the Diagonal
    for y in range(1, height + 1):
        diag_set = set()
        for x in range(1, width + 1):
            diag_set.add((x, y))
            y += 1
        diag_win = diag_set.issubset(player_moves)
        if diag_win is True:
            print("diagonal win")
        else:
            return False, None

# TODO: Check for a tie
# TODO: Otherwise the game isn't over


def main():
    height = 3
    width = 3
    win_condition = False
    player_moves = {()}
    comp_moves = {()}
    player_team = input_team()
    # assign comp_team all in one line using a ternary expression
    comp_team = 'O' if player_team == 'X' else 'X'

    while win_condition is False:
        # simple loop to render the board and get player move and computer move
        render_board(height, width, player_moves, player_team, comp_moves, comp_team)
        # add a move to the player set
        player_moves.add(user_move(height, width))
        comp_moves.add(comp_move(height, width))
        game_over(player_moves, comp_moves, width, height)
    if win_condition is True:
        print("Good Game, want to play another? (y/n)")


main()

# TODO: randomly choose an empty cell for the other team
# TODO: repeat until the game is over (win, loss, or tie)
