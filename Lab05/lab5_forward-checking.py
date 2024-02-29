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


def find_empty_cell(board, domains):
    empty_cells = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
    if empty_cells:
        cell = random.choice(empty_cells)
        row, col = cell
        domain = domains[row][col]
        return cell, domain
    return None, None


def update_domains(board, domains, row, col, num):
    for i in range(9):
        if num in domains[row][i]:
            domains[row][i].remove(num)
        if num in domains[i][col]:
            domains[i][col].remove(num)

    region_row, region_col = row // 3 * 3, col // 3 * 3
    for i in range(region_row, region_row + 3):
        for j in range(region_col, region_col + 3):
            if num in domains[i][j]:
                domains[i][j].remove(num)


def restore_domains(board, domains, row, col, num):

    for i in range(9):
        if board[row][i] == 0:
            domains[row][i].add(num)
        if board[i][col] == 0:
            domains[i][col].add(num)

    region_row, region_col = row // 3 * 3, col // 3 * 3
    for i in range(region_row, region_row + 3):
        for j in range(region_col, region_col + 3):
            if board[i][j] == 0:
                domains[i][j].add(num)


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
            update_domains(board, domains, row, col, num)
            if solve_sudoku(board, domains):
                return True
            board[row][col] = 0
            restore_domains(board, domains, row, col, num)

    return False


domains = [[set(range(1, 10)) for _ in range(9)] for _ in range(9)]


if solve_sudoku(board, domains):
    print_board(board)
else:
    print("No solution")
