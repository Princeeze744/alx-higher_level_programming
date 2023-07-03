#!/usr/bin/python3
"""N-queens algorithm module"""


def solve_nqueens(board, col, solution_list, n):
    """solve N-queen problem"""
    if col == n:
        save_board_config(board, n, solution_list)
        return

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueens(board, col + 1, solution_list, n)
            board[row][col] = 0


def is_safe(board, row, col, n):
    """check if row, column is safe"""
    i = row
    j = col
    while j >= 0:
        if board[i][j] == 1:
            return False
        j -= 1

    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i = row
    j = col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def make_board(n):
    """make of board NxN"""
    board = [[0 for x in range(n)] for x in range(n)]
    return board


def save_board_config(board, n, solution_list):
    """saves each config to solution list"""
    temp = []
    for row in range(n):
        for col in range(n):
            if board[row][col] == 1:
                temp.append([row, col])
    solution_list.append(temp)


def print_solutions(solution_list):
    """prints solution list"""
    for solution in solution_list:
        print(solution)


def main():
    """entry point"""
    from sys import argv
    try:
        n = int(argv[1])
        if n < 4:
            print("N must be at least 4")
            exit(1)
    except IndexError as idxerr:
        print("Usage: nqueens N")
        exit(1)
    except ValueError as verr:
        print("N must be a number")
        exit(1)

    solution_list = []
    board = make_board(int(n))
    solve_nqueens(board, 0, solution_list, n)
    print_solutions(solution_list)


if __name__ == "__main__":
    main()
