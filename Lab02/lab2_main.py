import time
import numpy as np

init = np.array([2, 5, 3, 1, 0, 6, 4, 7, 8])
last = -1


def init_matrix(init):
    return np.array(init).reshape((3, 3))


def is_final(st):
    contor = 1
    for i in range(3):
        for j in range(3):
            if st[i, j] != 0 and st[i, j] != contor:
                return 0
            elif st[i, j] != 0 and st[i, j] == contor:
                contor += 1
    return 1


def init_probl(st):
    matrix = np.zeros((3, 3), dtype=int)
    for i in range(0, len(init)):
        matrix[i // 3, i % 3] = init[i]
    return matrix


def search_zero(st):
    position = np.empty((1, 2), dtype=int)
    for i in range(3):
        for j in range(3):
            if st[i][j] == 0:
                position[0][0] = i
                position[0][1] = j
    return position


def validate_position(st, direction, position, last):
    if direction == -1 and 0 <= position[0, 1] - 1 < 3 and last != st[position[0, 0], position[0, 1] - 1]:
        st[position[0, 0], position[0, 1]], st[position[0, 0], position[0, 1] - 1] = st[
            position[0, 0], position[0, 1] - 1], st[position[0, 0], position[0, 1]]
        position[0, 1] -= 1
        if 0 <= position[0, 1] - 1 < 3:
            last = st[position[0, 0], position[0, 1] - 1]
        print_matrix(st)
        return 1
    elif direction == 1 and 0 <= position[0, 1] + 1 < 3 and last != st[position[0, 0], position[0, 1] + 1]:
        st[position[0, 0], position[0, 1]], st[position[0, 0], position[0, 1] + 1] = st[
            position[0, 0], position[0, 1] + 1], st[position[0, 0], position[0, 1]]
        position[0, 1] += 1
        if 0 <= position[0, 1] + 1 < 3:
            last = st[position[0, 0], position[0, 1] + 1]
        print_matrix(st)
        return 1
    elif direction == -2 and 0 <= position[0, 0] + 1 < 3 and last != st[position[0, 0] + 1, position[0, 1]]:
        st[position[0, 0], position[0, 1]], st[position[0, 0] + 1, position[0, 1]] = st[
            position[0, 0] + 1, position[0, 1]], st[position[0, 0], position[0, 1]]
        position[0, 0] += 1
        if 0 <= position[0, 0] + 1 < 3:
            last = st[position[0, 0] + 1, position[0, 1]]
        print_matrix(st)
        return 1
    elif direction == 2 and 0 <= position[0, 0] - 1 < 3 and last != st[position[0, 0] - 1, position[0, 1]]:
        st[position[0, 0], position[0, 1]], st[position[0, 0] - 1, position[0, 1]] = st[
            position[0, 0] - 1, position[0, 1]], st[position[0, 0], position[0, 1]]
        position[0, 0] -= 1
        if 0 <= position[0, 0] - 1 < 3:
            last = st[position[0, 0] - 1, position[0, 1]]
        print_matrix(st)
        return 1
    else:
        return 0


def move(st, direction, position):
    validate_position(st, direction, position)
    return st


def print_matrix(st):
    for i in range(3):
        for j in range(3):
            print(st[i, j], end=" ")
        print()
    print()


def copy_matrix(st):
    return np.copy(st)


def copy_position(position):
    return np.copy(position)


def iddfs(st, position, max_depth):
    for depth in range(max_depth):
        if dfs(st, position, depth) == 1:
            return 1
    return 0


def dfs(st, position, depth):
    if depth == 0:
        return 0
    if is_final(st):
        return 1
    for dir in [-1, 1, -2, 2]:
        copy_st = copy_matrix(st)
        copy_pos = copy_position(position)
        if validate_position(copy_st, dir, copy_pos, last):
            if dfs(copy_st, copy_pos, depth - 1) == 1:
                return 1
    return 0


st = init_probl(init)
print_matrix(st)
initial_position = search_zero(st)

start = time.time()
solution = iddfs(st, initial_position, max_depth=8)
end = time.time()

if solution == 1:
    print("Great!")
else:
    print("No solution!")

elapsed_time = (end - start)
print(f"Elapsed Time: {elapsed_time:.6f} seconds")
