from state import print_solution_path
from beam_search import beam_search
from puzzle import generate

from write_to_file import write_to_txt

puzzle = generate()

# print(puzzle)

# puzzle = [['1'], ['2', '5', '8'], ['X', '6', '3'], ['4', '7', '9']]
# puzzle = [['1'], ['7', '5', '4'], ['3', '6', '2'], ['8', '9', 'X']]

# puzzles = [generate(), generate()]

path, moves = beam_search(puzzle, 2)
path, moves = beam_search(puzzle, 3)

# if path:
    # print_solution_path(path)
