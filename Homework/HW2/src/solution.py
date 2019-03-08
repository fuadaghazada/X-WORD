from state import print_solution_path
from beam_search import beam_search
from puzzle import generate
from write_to_file import write_to_csv, write_to_txt

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
puzzles = generate_n_puzzles(1)

index = 1
path = None

# X and Y values for the puzzle solved with beam width 2 and 3
data = []

for puzzle in puzzles:
    path, num_moves_w2 = beam_search(puzzle, 2)
    path, num_moves_w3 = beam_search(puzzle, 3)

    data.append([index, num_moves_w2, num_moves_w3])
    index += 1

# Write puzzles (initial states) to txt
write_to_txt(puzzles)

# Writing result into csv file
write_to_csv(data)

# Print the trace for the last puzzle
if path:
    print_solution_path(path)
