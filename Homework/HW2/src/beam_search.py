from state import generate_next_states
from puzzle import GOAL

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

    queue = list()
    queue.append([puzzle])

    while len(queue) != 0:
        first = queue.pop(0)

        paths = []

        next_states = generate_next_states(first[-1])

        for state in next_states:
            path = tuple(first)

            # Rejecting paths with loops
            if state not in path:
                path = list(path)
                path.append(state)
                paths.append(path)

        # Adding new pathes to the 'front' of queue
        for path in paths:
            queue.append(path)

        # Check if goal is found!
        if len(queue) != 0 and GOAL in queue[0]:
            num_moves = len(queue[0]) - 1

            print("Solved! Here is the steps")
            print("Number of moves: ", num_moves, "\n")

            return queue[0], num_moves;

        elif len(queue) == 0:
            print("No path is found\n")

    return None;
