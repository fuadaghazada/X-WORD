from state import print_solution_path
from beam_search import beam_search
from puzzle import generate

'''
    Homework 2

    @authors: fuadaghazada, canozgurel
    @date: 7/3/2019
'''

'''
    Generating N distinct puzzles
'''
def generate_n_puzzles(n):
    distinct_puzzles = []

    while len(distinct_puzzles) != n:
        puzzle = generate()

        if puzzle not in distinct_puzzles:
            distinct_puzzles.append(puzzle)

    return distinct_puzzles


###### GENERATING 25 Distinct Puzzles #######
# puzzles = generate_n_puzzles(25)

puzzle = generate()

# puzzle = [['1'], ['2', '5', '8'], ['X', '6', '3'], ['4', '7', '9']]

path, num_moves = beam_search(puzzle, 2)

print_solution_path(path)

# path, num_moves = beam_search(puzzle, 3)
