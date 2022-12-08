import os

validInputs = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

#  grid indexing
#  0 | 1 | 2
# ---|---|---
#  3 | 4 | 5
# ---|---|---
#  6 | 7 | 8

# function that prints the board according to the format
def printGrid(grid):
    print(f'\t {grid[0]} | {grid[1]} | {grid[2]}')
    print('\t---|---|---')
    print(f'\t {grid[3]} | {grid[4]} | {grid[5]}')
    print('\t---|---|---')
    print(f'\t {grid[6]} | {grid[7]} | {grid[8]}')

# function that takes input from player X and appends 'X' at the index
def inputPlayerX(grid):
    valX = input('\nPlayer X\'s turn: ')[0]
    while valX not in validInputs:
        valX = input('INVALID INPUT - Enter again: ')
    grid[int(valX)] = 'X'
    return grid

# function that takes input from player O and appends 'O' at the index
def inputPlayerO(grid):
    valO = input('\nPlayer O\'s turn: ')[0]
    while valO not in validInputs:
        valO = input('INVALID INPUT - Enter again: ')
    grid[int(valO)] = 'O'
    return grid

# function that returns result after each iteration of input
def returnResult(grid):

    # set of indexes in grid
    remainingIndexes = set(grid)

    # loop to check horizontal win conditions
    i = 0
    while (i < 9):
        if grid[i] == grid[i+1] == grid[i+2] == 'X':
            return 'X'
        elif grid[i] == grid[i+1] == grid[i+2] == 'O':
            return 'O'
        i = i + 3

    # loop to check vertical win conditions
    i = 0
    while (i < 3):
        if grid[i] == grid[i + 3] == grid[i + 6] == 'X':
            return 'X'
        elif grid[i] == grid[i + 3] == grid[i + 6] == 'O':
            return 'O'
        i = i + 1

    # check diagonal win conditions
    if grid[0] == grid[4] == grid[8] == 'X':
        return 'X'
    elif grid[0] == grid[4] == grid[8] == 'O':
        return 'O'
    elif grid[2] == grid[4] == grid[6] == 'X':
        return 'X'
    elif grid[2] == grid[4] == grid[6] == 'O':
        return 'O'

    # draw conditions
    elif len(remainingIndexes) == 2:
        return 'D'

    # else continue to play
    else:
        return '-'

# main

while True:
    os.system('cls')

    # reset values in grid
    mainGrid = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

    for i in range(0, len(mainGrid)):
        os.system('cls')

        print('\n\t TicTacToe\n')

        printGrid(mainGrid)

        # get input
        if i % 2 == 0:
            grid = inputPlayerX(mainGrid)
        else:
            grid = inputPlayerO(mainGrid)

        # check result
        result = returnResult(mainGrid)
        if result == '-':
            continue
        elif result == 'X':
            os.system('cls')
            print('\n\tPLAYER X WINS!\n')
            input('\tpress enter key to play again...')
            break
        elif result == 'O':
            os.system('cls')
            print('\n\tPLAYER O WINS!\n')
            input('\tpress enter key to play again...')
            break
        elif result == 'D':
            os.system('cls')
            print('\n\tIT\'s a DRAW!\n')
            input('\tpress enter key to play again...')
            break
