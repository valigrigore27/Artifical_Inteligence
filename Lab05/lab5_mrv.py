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

def get_domain_length(cell):
    return len(domains[cell[0]][cell[1]])

def find_empty_cell(board, domains):
    empty_cells = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
    if empty_cells:
        empty_cells.sort(key=get_domain_length)
        cell = empty_cells[0]
        row, col = cell
        domain = domains[row][col]
        return cell, domain
    return None, None


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


def solve_sudoku(board, domains):
    empty_cell, domain = find_empty_cell(board, domains)
    if not empty_cell:
        return True

    row, col = empty_cell
    for num in list(domain):
        if is_valid_move(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board, domains):
                return True
            board[row][col] = 0

    return False


domains = [[set(range(1, 10)) for _ in range(9)] for _ in range(9)]


if solve_sudoku(board, domains):
    print_board(board)
else:
    print("No solution")
