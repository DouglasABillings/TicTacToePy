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
            block


player_team = input_team()

print(player_team)

# TODO: ask the user to choose aa team and store it
# TODO: ask the user for a move (x,y)
# TODO: re-render the game with their played move
# TODO: randomly choose an empty cell for the other team
# TODO: re-render the game
# TODO: repeat until the game is over (win, loss, or tie)
