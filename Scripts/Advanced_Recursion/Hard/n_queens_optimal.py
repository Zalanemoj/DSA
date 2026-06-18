class Solution:
    def solve(self, col, board, ans, leftover, upper_diagonal, lower_diagonal, n):
        if col == n:
            ans.append(board.copy())
            return

        for row in range(n):
            if (
                leftover[row] == 0
                and lower_diagonal[row+col] == 0
                and upper_diagonal[(n-1)+(col-row)] == 0
            ):
                board[row] = board[row][:col] + "Q" + board[row][col + 1:]
                leftover[row]=1
                lower_diagonal[row + col] = 1
                upper_diagonal[n - 1 + col - row] = 1

                self.solve(col + 1, board, ans, leftover, upper_diagonal, lower_diagonal, n)

                board[row] = board[row][:col] + "." + board[row][col + 1:]
                leftover[row] = 0
                upper_diagonal[n - 1 + col - row] = 0
                lower_diagonal[row + col] = 0


    def n_qeens(self,n:int):
        ans=[]
        board=["."*n for _ in range(n)]
        leftover= [0] * n
        upper_diagonal=[0]*(2*n-1)
        lower_diagonal=[0]*(2*n-1)

        self.solve(0, board, ans, leftover, upper_diagonal, lower_diagonal, n)

        return ans

sol = Solution()
print(sol.n_qeens(5))