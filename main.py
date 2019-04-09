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
    for x in range(1, height + 1):
        row = str(x)
        for y in range(1, width + 1):
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
    return (x, y)


def main():
    height = 3
    width = 3
    player_moves = {(3, 2)}
    comp_moves = {(3, 1)}
    player_team = input_team()
    # assign comp_team all in one line using a ternary expression
    comp_team = 'O' if player_team == 'X' else 'X'

    # render teh board
    render_board(height, width, player_moves, player_team, comp_moves, comp_team)
    # add a move to the player set
    player_moves.add(user_move(height, width))
    # render again
    render_board(height, width, player_moves, player_team, comp_moves, comp_team)


main()


# TODO: re-render the game with their played move
# TODO: randomly choose an empty cell for the other team
# TODO: re-render the game
# TODO: repeat until the game is over (win, loss, or tie)
