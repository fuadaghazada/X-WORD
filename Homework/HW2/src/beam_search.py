import math

from state import generate_next_states
from puzzle import GOAL, find_index

'''
    Searching for the solution

    @param:
        - given puzzle
        - beam width

    @return:
        - solution_path
        - number of moves
'''
def beam_search(puzzle, w):

    # Queue with one element
    queue = list()
    queue.append([puzzle])

    while len(queue) != 0:
        first = queue.pop(0)

        paths = []

        # Next states of the last node of the popped path
        next_states = generate_next_states(first[-1])

        for state in next_states:
            path = tuple(first)

            # Rejecting paths with loops
            if state not in path:
                path = list(path)
                path.append(state)
                paths.append({'path': path, 'h_value': len(path) + manhattan_distance(path[-1])})

        # Sorting according to heuristic value of path
        paths = sorted(paths, key = lambda k: k['h_value'])

        # Adding new pathes to the 'front' of queue
        for path in paths[:w]:
            queue.append(path['path'])

        # Check if goal is found!
        if len(queue) != 0 and GOAL in queue[0]:
            num_moves = len(queue[0]) - 1

            print('--------------------------')
            print("Solved with beam width: ", w)
            print("Number of moves: ", num_moves)
            print('--------------------------\n')

            return queue[0], num_moves;

        elif len(queue) == 0:
            print("No path is found\n")

    return None, None;


'''
    Finding manhattan_distance for a given puzzle
'''
def manhattan_distance(state):
    distance = 0

    for i in range(0, len(state)):
        for j in range(0, len(state[i])):
            value = state[i][j]

            if value is 'X':
                continue

            m, n = find_index(GOAL, value)

            distance += math.fabs(i - m)
            distance += math.fabs(j - n)

    return distance
