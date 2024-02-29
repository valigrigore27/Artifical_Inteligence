import random


def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()


board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


##

def find_empty_cell(board):
    empty_cells = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
    if empty_cells:
        return random.choice(empty_cells)
    return None


def is_valid_move(board, row, col, num):
    # linie
    if num in board[row]:
        return False

    # coloana
    if num in [board[i][col] for i in range(9)]:
        return False

    # regiune
    region_row, region_col = row // 3 * 3, col // 3 * 3
    for i in range(region_row, region_row + 3):
        for j in range(region_col, region_col + 3):
            if board[i][j] == num:
                return False
    return True


def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True

    row, col = empty_cell
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0

    return False


if solve_sudoku(board):
    print_board(board)
else:
    print("No solution")

