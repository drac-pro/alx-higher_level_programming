#!/usr/bin/python3
"""solve the n queen problem"""
import sys


class NQueens:
    """blueprint for the n queen board"""
    def solveNQueens(self, n: int):
        """solution to the n-queens problem
        Args:
            n(int): size of the of board
        """
        board = [[0] * n for _ in range(n)]
        result = []

        used_col = set()
        used_diagonals = set()
        used_antidiagonals = set()

        def backtrack(row):
            """bactracking funtion to fin solutions for n-queens
            Args:
                row(int): row on the board
            """
            if row == n:
                solution = []
                for i in range(n):
                    for j in range(n):
                        if board[i][j] == 1:
                            solution.append([i, j])
                result.append(solution)
                return
            for col in range(n):
                if not (col in used_col or (row - col) in used_diagonals or
                        (row + col) in used_antidiagonals):
                    used_col.add(col)
                    used_diagonals.add(row - col)
                    used_antidiagonals.add(row + col)
                    board[row][col] = 1
                    backtrack(row + 1)

                    used_col.remove(col)
                    used_diagonals.remove(row - col)
                    used_antidiagonals.remove(row + col)
                    board[row][col] = 0
        backtrack(0)
        return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solution = NQueens()
    result = solution.solveNQueens(N)
    for solution in result:
        print(solution)
