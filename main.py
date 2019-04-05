# What we want a tic tac toe grid to look like
#  123
# 1###
# 2###
# 3###


def render_board(height, width, player_move, player_team, comp_move, comp_team):
    # Render the first row of indexes
    index_row = " "
    for n in range(1, width + 1):
        index_row += str(n)
    print(index_row)

    # Render the game grid
    for x in range(1, height + 1):
        row = str(x)
        for y in range(1, width + 1):
            if (x, y) in player_move:
                row += player_team
            elif (x, y) in comp_move:
                row += comp_team
            else:
                row += '#'
        print(row)


def input_team():
    # user team option
    team_var = ''
    while team_var is not 'X' or 'O':
        team_var = input("Choose a team, X's or O's\n").upper()

        if team_var == 'X' or team_var == 'O':
            return team_var


def user_move(height, width):
    # tuple for user prompt
    x, y = 0, 0
    while x not in range(1, height + 1):
        while y not in range(1, width + 1):
            try:
                # We have to handle this in a try catch block, because it may throw an exception
                x, y = map(int, input("Please enter your move in the form of x y\n").split())
            except ValueError:
                # Make sure to handle a ValueError exception
                x, y = (0, 0)
    return {(x, y)}


def main():
    height = 3
    width = 3
    player_move = {(3, 2)}
    comp_move = {(3, 1)}
    comp_team = None
    player_team = input_team()
    comp_team = 'O' if player_team == 'X' else comp_team == 'X'
    render_board(height, width, player_move, player_team, comp_move, comp_team)
    player_move = user_move(height, width)
    render_board(height, width, player_move, player_team, comp_move, comp_team)


main()


# TODO: re-render the game with their played move
# TODO: randomly choose an empty cell for the other team
# TODO: re-render the game
# TODO: repeat until the game is over (win, loss, or tie)
