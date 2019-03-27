# What we want a tic tac toe grid to look like
#  123
# 1###
# 2###
# 3###

# Here the width and height of the grid
height = 3
width = 3

# Render the first row of indexes
index_row = " "
for n in range(1, width + 1):
    index_row += str(n)
print(index_row)

# Render the game grid
for h in range(1, height + 1):
    row = str(h)
    for n in range(1, width + 1):
        row += '#'
    print(row)


def input_team():
    # user team option
    team = ''
    while team is not 'x' or 'o':
        team = input("Choose a team, X's or O's\n").lower()

        if team == 'x' or team == 'o':
            return team


def user_move():
    # tuple for user prompt
    x, y = 0, 0
    while x not in range(1, height + 1):
        while y not in range(1, width + 1):
            try:
                # We have to handle this in a try catch block, because it may throw an exception
                x, y = map(int, input("Please enter your move in the form of x y\n").split())
            except ValueError:
                # Make sure to handle a ValueError exception
                x, y = 0, 0
    return x, y


player_team = input_team()

print(player_team)
move = user_move()

print(move)

# TODO: re-render the game with their played move
# TODO: randomly choose an empty cell for the other team
# TODO: re-render the game
# TODO: repeat until the game is over (win, loss, or tie)
