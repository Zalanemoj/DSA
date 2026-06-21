from copy import deepcopy
from typing import List
from collections import deque

class Solution:
    """This is a class in order to solve the rotten orange problem"""

    def solve(self,mat:List[List[int]],minutes:int,fresh_count:int)-> None:
        """This function solves the rotten orange problem"""
        rows,cols=len(mat),len(mat[0])
        queue=deque()
        # Copying the whole metric so that we can make changes in that
        grid=deepcopy(mat)

        # Iterating in order to find the fresh count as well as the rotten values
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    queue.append([i,j])
                elif grid[i][j]==1:
                    fresh_count+=1

        # Uh iterating through the rotten values kind of
        while queue and fresh_count>0:
            minutes+=1
            total_roten=len(queue)

            for _ in range(total_roten):
                # Popping out values of the queue
                i,j=queue.popleft()

                # Iterating in all the four direction in order to find the good oranges
                for dx,dy in [(-1,0),(0,1),(1,0),(0,-1)]:
                    new_i,new_j=i+dx,j+dy
                    # Scenarios row or column gets out of bound
                    if new_i<0 or new_j<0 or new_i == rows or new_j == cols:
                        continue
                    if grid[new_i][new_j]==2 or grid[new_i][new_j]==0:
                        continue
                    fresh_count-=1
                    grid[new_i][new_j]=2
                    queue.append([new_i,new_j])

    def rotten_oranges(self)->int:
        """This function is an initialization of all the variables in order to solve the problem"""
        #Initializing all the variables
        matrix=[[2,1,1],[1,1,0],[0,1,1]]
        minutes=0
        fresh_count=0

        #Calling the function
        self.solve(matrix,minutes,fresh_count)

        # Edge Case
        if fresh_count>0:
            return -1

        # Written number of minutes
        return minutes

