import math

from puzzle import find_index, find_possible_moves, move, GOAL

'''
    Finding manhattan_distance for a given puzzle
'''
def manhattan_distance(puzzle):
    distance = 0

    for i in range(0, len(puzzle)):
        for j in range(0, len(puzzle[i])):
            value = puzzle[i][j]

            if value is 'X':
                continue

            m, n = find_index(GOAL, value)

            distance += math.fabs(i - m)
            distance += math.fabs(j - n)

    return distance


'''
    Generating next states for the given state of puzzle

    Note: states are sorted according to their distance (Manhattan) to goal
'''
def generate_next_states(puzzle):

    next_states = []
    moves = find_possible_moves(puzzle)

    for m in moves:
        state = move(puzzle, m)
        m_dist = manhattan_distance(state)
        next_states.append({'state' : state, 'distance': m_dist})

    # Sorting the list according to distance
    next_states = sorted(next_states, key = lambda k: k['distance'])

    temp = []
    for state in next_states:
        temp.append(state['state'])

    return temp


'''
    Get the move type between 2 states: from state1 to state2
'''
def move_statement(state1, state2):
    (i1, j1) = find_index(state1, 'X')
    (i2, j2) = find_index(state2, 'X')

    dh = j2 - j1
    dv = i2 - i1

    moved_tile = state1[i2][j2]
    statement = str(moved_tile) + " moved "

    if dh == 1:
        statement += 'left'
    elif dh == -1:
        statement += 'right'
    elif dv == 1:
        statement += 'up'
    elif dv == -1:
        statement += 'down'
    else:
        statement = ""

    return statement + "\n"


'''
    Printing the puzzle state in a pretty format
'''
def print_state(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            print(state[i][j], end = '\t')
        print('\n')


'''
    Printing the solution path
'''
def print_solution_path(path):
    cur_state = None
    for state in path:
        if cur_state:
            print(move_statement(cur_state, state))
        print_state(state)
        print("-----------------")
        cur_state = state
