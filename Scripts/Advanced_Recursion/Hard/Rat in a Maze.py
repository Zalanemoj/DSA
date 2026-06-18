from typing import List
matrix=[[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]

class Solution:
    def path_finder(self,
                    row: int,
                    col: int,
                    mat: List[List[int]],
                    n:int,
                    ans:List[str],
                    move:str,
                    visit:List[List[int]]
                    ):
        if row == n-1 and col == n-1:
            ans.append(move)
            return

        if row + 1 < n and not visit[row+1][col] and mat[row + 1][col] == 1:
            visit[row][col] = 1
            self.path_finder(row+1, col, mat,n, ans, move + "D", visit)
            visit[row][col] = 0

        if col - 1 >= 0 and not visit[row][col - 1] and mat[row][col - 1] == 1:
            visit[row][col] = 1
            self.path_finder(row, col - 1, mat,n, ans, move + "L", visit)
            visit[row][col] = 0

        if col + 1 < n and not visit[row][col + 1] and mat[row][col + 1] == 1:
            visit[row][col] = 1
            self.path_finder(row, col + 1, mat,n, ans, move + "R", visit)
            visit[row][col] = 0

        if row - 1 >= 0 and not visit[row - 1][col] and mat[row - 1][col] == 1:
            visit[row][col] = 1
            self.path_finder(row - 1, col, mat,n, ans, move + "U", visit)
            visit[row][col] = 0

    def rat_maze(self,matrix: List[List[int]]) -> List[str]:
        ans = []
        n=len(matrix)
        vis=[[0 for _ in range(n)] for _ in range(n)]

        if matrix[0][0]==1:
            self.path_finder(0,0,matrix,n,ans,"",vis)
        return ans

sol = Solution()
print(sol.rat_maze(matrix))