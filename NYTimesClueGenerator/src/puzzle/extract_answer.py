import numpy as np

'''
    Extracts the answer from the puzzle according to the given number
    for across or down clue

    @param: puzzle - given puzzle
    @param: num - number for clue
    @type: type of clue: 0 for across | 1 for down
'''
def find_answer_with_clue_num(puzzle, num, type = 0):
    grid = np.array(puzzle)

    a, b = -1, -1
    for i in range(grid.shape[1]):
        for j in range(grid.shape[0]):
            if grid[i][j] is not None and str(num) in grid[i][j]:
                a, b = i, j
                break

    word = None
    if (a, b) != (-1, -1):
        if type == 0:
            word = grid[a, :]
        else:
            word = grid[:, b]

    answer = ""
    if word is not None:
        for el in word:
            answer += el[-1] if el is not None else ""

    return answer

'''
    Extract all answers from clues according
    to the given crossword data

    @param: data - given crossword data
'''
def extract_answers_from_clues(data):

    puzzle, clues = data['puzzle'], data['clues']

    across = []
    for clue in clues['across']:
        answer = find_answer_with_clue_num(puzzle, clue['number'], 0)
        across.append({'clue': clue['clue'], 'answer': answer, 'number': clue['number']})

    down = []
    for clue in clues['down']:
        answer = find_answer_with_clue_num(puzzle, clue['number'], 1)
        down.append({'clue': clue['clue'], 'answer': answer, 'number': clue['number']})

    return {"across": across, "down": down}
