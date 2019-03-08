from state import print_solution_path
from beam_search import beam_search
from puzzle import generate

from write_to_file import write_to_txt

puzzle = generate()

puzzles = [generate(), generate()]


#
# path, moves = beam_search(puzzle, 2)
#
# if path:
#     print_solution_path(path)

# puzzle = [['1'], ['2', '5', '8'], ['X', '6', '3'], ['4', '7', '9']]
