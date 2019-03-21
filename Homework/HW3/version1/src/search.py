import math
import copy

from state import generate_next_states
from puzzle import GOAL, find_index

'''
    Branch and Bound Search
'''
def BBS(puzzle):

    # Queue with one element
    queue = list()
    queue.append({'path': [puzzle], 'h_value': 0})

    while len(queue) != 0:
        first = queue.pop(0)

        paths = []

        # Next states of the last node of the popped path
        next_states = generate_next_states(first['path'][-1])

        for state in next_states:
            path = tuple(first['path'])

            # Rejecting paths with loops
            if state not in path:
                path = list(path)
                path.append(state)
                paths.append({'path': path, 'h_value': len(path)})

        # Adding paths to the queue
        for path in paths:
            queue.append(path)

        # Sorting the queue by path cost
        queue = sorted(queue, key = lambda k: k['h_value'])

        # Check if goal is found!
        if len(queue) != 0 and GOAL in queue[0]['path']:
            num_moves = len(queue[0]['path']) - 1

            print('--------------------------')
            print("Solved with BBS")
            print("Number of moves: ", num_moves)
            print('--------------------------\n')

            return queue[0]['path'], num_moves;

        elif len(queue) == 0:
            print("No path is found\n")

    return None, None;


'''
    A* search
'''
def A_star_search(puzzle):

    # Queue with one element
    queue = list()
    queue.append({'path': [puzzle], 'h_value': eucledian_distance(puzzle)})

    while len(queue) != 0:
        first = queue.pop(0)

        paths = []

        # Next states of the last node of the popped path
        next_states = generate_next_states(first['path'][-1])

        for state in next_states:
            path = tuple(first['path'])

            # Rejecting paths with loops
            if state not in path:
                path = list(path)
                path.append(state)
                paths.append({'path': path, 'h_value': len(path) + eucledian_distance(path[-1])})

        # Adding paths to the queue
        for path in paths:
            queue.append(path)

        # Sorting the queue by path cost
        queue = sorted(queue, key = lambda k: k['h_value'])

        # Removing redundant paths with the same reaching node
        temp = []
        reach_nodes = []

        for path in queue:
            if path['path'][-1] not in reach_nodes:
                reach_nodes.append(path['path'][-1])
                temp.append(path)

        queue = copy.deepcopy(temp)

        # Check if goal is found!
        if len(queue) != 0 and GOAL in queue[0]['path']:
            num_moves = len(queue[0]['path']) - 1

            print('--------------------------')
            print("Solved with A*")
            print("Number of moves: ", num_moves)
            print('--------------------------\n')

            return queue[0]['path'], num_moves;

        elif len(queue) == 0:
            print("No path is found\n")

    return None, None;

'''
    Finding Eucledian distance of the given state from goal
'''
def eucledian_distance(state):
    distance = 0

    for i in range(0, len(state)):
        for j in range(0, len(state[i])):
            value = state[i][j]

            if value is 'X':
                continue

            m, n = find_index(GOAL, value)

            distance += math.sqrt((i - m) * (i - m) + (j - n) * (j - n))

    return distance
