from puzzle import find_index, find_possible_moves, move, GOAL

'''
    Generating next states for the given state of puzzle

    Note: states are sorted according to their distance (Manhattan) to goal
'''
def generate_next_states(puzzle):

    next_states = []
    moves = find_possible_moves(puzzle)

    for m in moves:
        state = move(puzzle, m)
        next_states.append(state)

    return next_states


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
    print('-----')
    for i in state:
        for j in i:
            if j is i[0]:
                print('| ', end='')
            print(j + ' | ', end='')
        print('\n-------------')
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
