from typing import List

class Solution:

    def is_safe(self, row, col, board, n):

        duprow = row
        dupcol = col

        # upper-left diagonal
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1

        # left side
        row = duprow
        col = dupcol

        while col >= 0:
            if board[row][col] == "Q":
                return False
            col -= 1

        # lower-left diagonal
        row = duprow
        col = dupcol

        while row < n and col >= 0:
            if board[row][col] == "Q":
                return False
            row += 1
            col -= 1

        return True

    def solve(self, col, board, ans, n):

        if col == n:
            ans.append(board.copy())
            return

        for row in range(n):

            if self.is_safe(row, col, board, n):

                board[row] = (
                    board[row][:col]
                    + "Q"
                    + board[row][col + 1:]
                )

                self.solve(col + 1, board, ans, n)

                board[row] = (
                    board[row][:col]
                    + "."
                    + board[row][col + 1:]
                )

    def solve_n_queens(self, n: int) -> List[List[str]]:

        ans = []

        board = ["." * n for _ in range(n)]

        self.solve(0, board, ans, n)

        return ans


sol = Solution()
print(sol.solve_n_queens(4))