# Import libraries
from collections import deque
from typing import List

class DepthFirstSearch:
    """Class that implements a depth first search algorithm"""

    def solve(self,node:int,adj:List[List[int]],result:List[int],visit:List[int]) -> None:
        """This function implements a depth first search algorithm"""
        result.append(node)
        visit[node]=1

        # Iterating for Each and every node in the adjacency list
        for neighbour in adj[node]:
            #  If the node is not visited then only
            if visit[neighbour]==0:
                self.solve(neighbour,adj,result,visit)

    def dfs(self) -> List[int]:
        """This function declares all the variable and returns the result of depth first search algorithm"""

        # Declaring all the variables
        adjacency_list=[[], [2, 3], [1, 4], [4, 1, 5], [2, 3, 5], [3, 4]]
        total_nodes=len(adjacency_list)
        visited_nodes=[0]*total_nodes
        result=[]

        # Calling the function in order to find the result
        self.solve(1,adjacency_list,result,visited_nodes)

        # Returning the result in list format containing all the integers in a specific order
        return result

#region Printing
sol=DepthFirstSearch()
print(sol.dfs())
#endregion

