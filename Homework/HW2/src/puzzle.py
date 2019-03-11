import random
import copy

# Goal puzzle
GOAL = [['X'],
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']]

'''
    Generating random puzzle
'''
def generate():
    no_steps = random.randint(25, 30)

    puzzle = copy.deepcopy(GOAL)

    # Moving empty slot random number of times
    for i in range(no_steps):
        puzzle = move_random(puzzle)

    return puzzle


'''
    Finding any tile indices from the puzzle
'''
def find_index(puzzle, value):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == value:
                return (i, j)
    return None


'''
    Finding neighbors of a tile with the given index
    in the puzzle
'''
def find_possible_moves(puzzle):
    # Location of empty slot
    (i, j) = find_index(puzzle, 'X')

    # Possible moves
    moves = []

    # Up
    if i > 1 or (i == 1  and j == 0):
        moves.append('up')

    # Down
    if i < len(puzzle) - 1:
        moves.append('down')

    # Right
    if i > 0 and j < len(puzzle[i]) - 1:
        moves.append('right')

    # Left
    if i > 0 and j > 0:
        moves.append('left')

    return moves


'''
    Randomly move the empty tile to an available spot
'''
def move_random(puzzle):
    # Possible moves
    moves = find_possible_moves(puzzle)

    # Choice index
    choice = moves[random.randint(0, len(moves) - 1)]

    # Moving the tile according to random choice
    return move(puzzle, choice)


'''
    Moving a tile in the given direction
'''
def move(puzzle, dir):
    # Location of Empty slot
    (x_i, x_j) = find_index(puzzle, 'X')

    puzzle_cp = copy.deepcopy(puzzle)

    # Apply move
    if dir is 'up':
        puzzle_cp[x_i - 1][x_j], puzzle_cp[x_i][x_j] = puzzle_cp[x_i][x_j], puzzle_cp[x_i - 1][x_j]
    elif dir is 'down':
        puzzle_cp[x_i + 1][x_j], puzzle_cp[x_i][x_j] = puzzle_cp[x_i][x_j], puzzle_cp[x_i + 1][x_j]
    elif dir is 'right':
        puzzle_cp[x_i][x_j + 1], puzzle_cp[x_i][x_j] = puzzle_cp[x_i][x_j], puzzle_cp[x_i][x_j + 1]
    elif dir is 'left':
        puzzle_cp[x_i][x_j - 1], puzzle_cp[x_i][x_j] = puzzle_cp[x_i][x_j], puzzle_cp[x_i][x_j - 1]

    return puzzle_cp
