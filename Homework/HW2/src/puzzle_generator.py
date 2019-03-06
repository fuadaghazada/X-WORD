import random

'''
    Puzzle generator

    @authors: fuadaghazada, canozgurel
    @date: 7/3/2019
'''

class PuzzleGenerator:

    '''
        Generating N distinct puzzles
    '''
    def generate_n_puzzles(self, n):
        distinct_puzzles = []

        while len(distinct_puzzles) != n:
            puzzle = self.generate()

            if puzzle not in distinct_puzzles:
                distinct_puzzles.append(puzzle)

        return distinct_puzzles


    '''
        Generating random puzzle
    '''
    def generate(self):
        puzzle =  [['X'],
                  ['1', '2', '3'],
                  ['4', '5', '6'],
                  ['7', '8', '9']]

        no_steps = random.randint(50, 100)

        # Moving empty slot random number of times
        for i in range(no_steps):
            self.__move_random(puzzle)

        return puzzle


    '''
        Finding empty tile from the puzzle
    '''
    def __find_x(self, puzzle):
        for i in range(len(puzzle)):
            for j in range(len(puzzle[i])):
                if puzzle[i][j] == 'X':
                    return (i, j)
        return None


    '''
        Finding neighbors of a tile with the given index
        in the puzzle
    '''
    def __find_possible_moves(self, puzzle, i, j):
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
    def __move_random(self, puzzle):
        # Location of Empty slot
        (x_i, x_j) = self.__find_x(puzzle)

        # Possible moves
        moves = self.__find_possible_moves(puzzle, x_i, x_j)

        # Choice index
        choice = moves[random.randint(0, len(moves) - 1)]

        # Apply move
        if choice is 'up':
            puzzle[x_i - 1][x_j], puzzle[x_i][x_j] = puzzle[x_i][x_j], puzzle[x_i - 1][x_j]
        elif choice is 'down':
            puzzle[x_i + 1][x_j], puzzle[x_i][x_j] = puzzle[x_i][x_j], puzzle[x_i + 1][x_j]
        elif choice is 'right':
            puzzle[x_i][x_j + 1], puzzle[x_i][x_j] = puzzle[x_i][x_j], puzzle[x_i][x_j + 1]
        elif choice is 'left':
            puzzle[x_i][x_j - 1], puzzle[x_i][x_j] = puzzle[x_i][x_j], puzzle[x_i][x_j - 1]
