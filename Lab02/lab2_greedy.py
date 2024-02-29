import time
import numpy as np

# init = np.array([2, 5, 3, 1, 0, 6, 4, 7, 8])
init = np.array([2, 1, 3, 4, 5, 6, 7, 8, 0])


def init_matrix(init):
    return np.array(init).reshape((3, 3))


def is_final(st):
    return np.array_equal(st, np.sort(st, axis=None))


def init_probl(st):
    matrix = np.zeros((3, 3), dtype=int)
    for i in range(0, len(init)):
        matrix[i // 3, i % 3] = init[i]
    return matrix


def search_zero(st):
    position = np.argwhere(st == 0)
    return position[0]


def print_matrix(st):
    for i in range(3):
        for j in range(3):
            print(st[i, j], end=" ")
        print()
    print()


def manhattan_distance(cell_value, current_position, final_positions):
    if cell_value == 0:
        return 0
    final_position = final_positions[cell_value - 1]
    return abs(final_position[0] - current_position[0]) + abs(final_position[1] - current_position[1])


def greedy(st, position):
    if is_final(st):
        return 1

    possible_moves = [-1, 1, -3, 3]  # Left, Right, Up, Down

    possible_moves.sort(key=lambda move: manhattan_distance(st[position[0], position[1]], position, final_positions))

    for move in possible_moves:
        new_position = position + move
        if 0 <= new_position[0] < 3 and 0 <= new_position[1] < 3:
            copy_st = st.copy()
            copy_st[position[0], position[1]] = copy_st[new_position[0], new_position[1]]
            copy_st[new_position[0], new_position[1]] = 0
            if manhattan_distance(copy_st[position[0], position[1]], position, final_positions) < manhattan_distance(
                    st[position[0], position[1]], position, final_positions):
                if greedy(copy_st, new_position):
                    return 1
    return 0


st = init_probl(init)
print_matrix(st)
initial_position = search_zero(st)

# Calculate final positions for the cells
final_positions = [np.argwhere(st == i)[0] for i in range(1, 9)]

start = time.time()
solution = greedy(st, initial_position)
end = time.time()

if solution == 1:
    print("Great!!")
else:
    print("No solution!")

elapsed_time = (end - start)
print(f"Elapsed Time: {elapsed_time:.6f} seconds")
