#!/usr/bin/python3
"""Script writes a program that solves the N queens problem."""
import sys


def is_safe(board, row, col, N):
    # Check if a queen can be placed at the current position (row, col)
    for i in range(row):
        if board[i] == col or \
           abs(board[i] - col) == abs(i - row):
            return False
    return True


def print_solution(board):
    # Print the board configuration for a solution
    N = len(board)
    for i in range(N):
        line = ["Q" if j == board[i] else "." for j in range(N)]
        print(" ".join(line))


def solve_nqueens(N):
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N

    def backtrack(row):
        if row == N:
            print_solution(board)
            print()
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    N = sys.argv[1]
    solve_nqueens(N)


# def n_queen(n):
#     """Return all possible arrange for the n-queen problem."""
#     col = set()
#     pos = set()
#     neg = set()
#     res = []
#     state = []

#     def backtrack(r):
#         """Backtrack using recursion"""
#         if r == n:
#             res.append([val for val in state])
#         for c in range(n):
#             if c in col or (r + c) in pos or (r - c) in neg:
#                 continue
#             col.add(c)
#             pos.add(r + c)
#             neg.add(r - c)
#             state.append([r, c])

#             backtrack(r + 1)

#             col.remove(c)
#             pos.remove(r + c)
#             neg.remove(r - c)
#             state.pop()
#     backtrack(0)
#     return res


# def main():
#     """Main Entry"""
#     if len(sys.argv) != 2:
#         print("Usage: nqueens N")
#         sys.exit(1)

#     n = sys.argv[1]
#     try:
#         n = int(n)
#     except ValueError:
#         print("N must be a number")
#         sys.exit(1)

#     if n < 4:
#         print("N must be at least 4")
#         sys.exit(1)

#     for res in n_queen(n):
#         print(res)


# main()
