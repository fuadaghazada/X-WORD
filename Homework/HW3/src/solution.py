from state import print_solution_path
from search import BBS, A_star_search
from puzzle import generate
from write_to_file import write_to_csv, write_to_txt

'''
    CS461 - Artificial Intelligence Homework 3

    Group members:
        * Fuad Aghazada
        * Can Özgürel
        * Çağatay Sel
        * Utku Mert Topçuoğlu
        * Kaan Kıranbay

    As heuristic function
        h (sum of Eucledian distances of the tiles from their goal positions)
        has been used

    @authors: fuadaghazada, canozgurel
    @date: 21/3/2019
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
puzzles = generate_n_puzzles(25)

index = 1
path = None

# X and Y values for the puzzle solved with BBS and A*
data = []

for puzzle in puzzles:
    path, num_moves_bbs = BBS(puzzle)
    path, num_moves_a_star = A_star_search(puzzle)

    data.append([index, num_moves_bbs, num_moves_a_star])
    index += 1

# Write puzzles (initial states) to txt
write_to_txt(puzzles)

# Writing result into csv file
write_to_csv(data)

# Print the trace for the last puzzle
print("\n\n----Solution trace for last puzzle!----\n\n")
if path:
    print_solution_path(path)
