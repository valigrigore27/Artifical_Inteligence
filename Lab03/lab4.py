import time
from threading import Thread, Lock
import numpy as np

def init_matrix(init):
    return np.array(init).reshape((3, 3))

def search_zero(st):
    position = np.argwhere(st == 0)
    return position.flatten()

def manhattan_distance(st):
    goal_state = np.array([1, 2, 3, 4, 5, 6, 7, 8, 0]).reshape((3, 3))
    distance = 0

    for i in range(1, 9):
        goal_position = np.argwhere(goal_state == i)[0]
        current_position = np.argwhere(st == i)[0]

        distance += abs(goal_position[0] - current_position[0]) + abs(goal_position[1] - current_position[1])

    return distance

def hamming_distance(st):
    goal_state = np.array([1, 2, 3, 4, 5, 6, 7, 8, 0])
    goal_state = goal_state.reshape(st.shape)
    misplaced_tiles = np.count_nonzero(st.flatten()[:-1] != goal_state.flatten()[:-1])
    return misplaced_tiles

def chebyshev_distance(st):
    goal_state = np.array([1, 2, 3, 4, 5, 6, 7, 8, 0]).reshape(st.shape)
    distance = np.max(np.abs(st - goal_state))
    return distance

def copy_matrix(st):
    return np.copy(st)

def copy_position(position):
    return np.copy(position)

def validate_position(st, direction, position, last):
    if direction == -1 and 0 <= position[1] - 1 < 3 and last != st[position[0], position[1] - 1]:
        st[position[0], position[1]], st[position[0], position[1] - 1] = st[position[0], position[1] - 1], st[position[0], position[1]]
        position[1] -= 1
        if 0 <= position[1] - 1 < 3:
            last = st[position[0], position[1] - 1]

        return 1
    elif direction == 1 and 0 <= position[1] + 1 < 3 and last != st[position[0], position[1] + 1]:
        st[position[0], position[1]], st[position[0], position[1] + 1] = st[position[0], position[1] + 1], st[position[0], position[1]]
        position[1] += 1
        if 0 <= position[1] + 1 < 3:
            last = st[position[0], position[1] + 1]

        return 1
    elif direction == -2 and 0 <= position[0] + 1 < 3 and last != st[position[0] + 1, position[1]]:
        st[position[0], position[1]], st[position[0] + 1, position[1]] = st[position[0] + 1, position[1]], st[position[0], position[1]]
        position[0] += 1
        if 0 <= position[0] + 1 < 3:
            last = st[position[0] + 1, position[1]]

        return 1
    elif direction == 2 and 0 <= position[0] - 1 < 3 and last != st[position[0] - 1, position[1]]:
        st[position[0], position[1]], st[position[0] - 1, position[1]] = st[position[0] - 1, position[1]], st[position[0], position[1]]
        position[0] -= 1
        if 0 <= position[0] - 1 < 3:
            last = st[position[0] - 1, position[1]]

        return 1
    else:
        return 0

def is_final(st):
    contor = 1
    for i in range(3):
        for j in range(3):
            if st[i, j] != 0 and st[i, j] != contor:
                return 0
            elif st[i, j] != 0 and st[i, j] == contor:
                contor += 1
    return 1

def print_matrix(st):
    for i in range(3):
        for j in range(3):
            print(st[i, j], end=" ")
        print()
    print()

def iddfs(st, position, lock, heuristic=None):
    max_depth = 10
    moves = 0
    for depth in range(max_depth):
        solution,moves = dfs(st, position, depth, moves + 1)
        if solution != 0:
            return moves
    return 0

def dfs(st, position, depth, moves):
    if depth == 0:
        return 0,moves + 1
    if is_final(st):
        return 1,moves + 1
    for dir in [-1, 1, -2, 2]:
        copy_st = copy_matrix(st)
        copy_pos = copy_position(position)
        moves += 1
        if validate_position(copy_st, dir, copy_pos, last):
            if dfs(copy_st, copy_pos, depth - 1,moves) != 0:
                return 1,moves + 1
    return 0,moves

def greedy(st, position, lock, heuristic):
    pr_queue = [(heuristic(st), st.tolist())]
    visited = set()
    moves = 0

    while pr_queue:
        _, current_state = pr_queue.pop(0)

        current_state_tuple = tuple(map(tuple, current_state))
        if is_final(np.array(current_state)):
            return moves
        visited.add(current_state_tuple)

        for direction in [-1, 1, -2, 2]:
            new_state = np.array([row[:] for row in current_state])
            new_position = search_zero(new_state)
            if validate_position(new_state, direction, new_position, last):
                new_state_tuple = tuple(map(tuple, new_state.tolist()))
                if new_state_tuple not in visited:
                    moves += 1
                    pr_queue.append((heuristic(new_state), new_state.tolist()))
        pr_queue.sort(key=lambda x: x[0])

    return 0

def run(alg, st, heuristic=None, lock=None):
    start_time = time.time()
    solution = alg(st, initial_position, lock, heuristic)
    end_time = time.time()

    if solution:
        print(f"Solution {alg.__name__} with {heuristic.__name__ if heuristic else 'no Heuristic'}:")
        print(f"{solution} moves")
        print(f"Execution time: {end_time - start_time:.6f} seconds.\n")
    else:
        print(f"No solution {alg.__name__} with {heuristic.__name__ if heuristic else 'No Heuristic'}.\n")

init = np.array([2, 5, 3, 1, 0, 6, 4, 7, 8])
st = init_matrix(init)
print_matrix(st)
initial_position = search_zero(st)
last = -1
last_lock = Lock()
last_moves = None

threads = [
    Thread(target=run, args=(iddfs, st, None, last_lock)),
    Thread(target=run, args=(greedy, st,manhattan_distance, last_lock)),
    Thread(target=run, args=(greedy, st,hamming_distance, last_lock)),
    Thread(target=run, args=(greedy, st,chebyshev_distance, last_lock)),
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()