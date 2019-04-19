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
        if row_set.issubset(player_moves):
            return True, "Player"
        elif row_set.issubset(comp_moves):
            return True, "Computer"
    # Checking the Columns
    for x in range(1, width + 1):
        col_set = set()
        for y in range(1, height + 1):
            col_set.add((x, y))
        if col_set.issubset(player_moves):
            return True, "Player"
        elif col_set.issubset(comp_moves):
            return True, "Computer"
    # Checking the Diagonal
    first_diag_set = set()
    second_diag_set = set()
    for x in range(1, height + 1):
        first_diag_set.add((x, x))
        second_diag_set.add((x, width + 1 - x))
    if first_diag_set.issubset(player_moves) or second_diag_set.issubset(player_moves):
        print("diagonal win")
    elif first_diag_set.issubset(comp_moves) or second_diag_set.issubset(comp_moves):
        return True, "Computer"
    if len(player_moves.union(comp_moves)) == width * height:
        return True, None
    else:
        return False, None


def main():
    width = height = 3
    is_over = False
    player_moves = set()
    comp_moves = set()
    player_team = input_team()
    # assign comp_team all in one line using a ternary expression
    comp_team = 'O' if player_team == 'X' else 'X'

    while not is_over :
        # simple loop to render the board and get player move and computer move
        render_board(height, width, player_moves, player_team, comp_moves, comp_team)

        # add a move to the player set
        move = user_move(height, width)
        while move in player_moves.union(comp_moves):
            move = user_move(height, width)
        player_moves.add(move)

        move = comp_move(height, width)
        while move in comp_moves.union(player_moves):
            move = comp_move(height, width)
        comp_moves.add(move)

        is_over, winning_player = game_over(player_moves, comp_moves, width, height)

    print("Good Game " + winning_player)


if __name__ == "__main__":
    # execute only if run as a script
    main()

# TODO: randomly choose an empty cell for the other team
# TODO: repeat until the game is over (win, loss, or tie)
