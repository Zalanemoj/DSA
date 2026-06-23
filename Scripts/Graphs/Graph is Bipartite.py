# importing all the libraries
from typing import List
from collections import deque
from datetime import *

# Starting time of running the program
start_time = datetime.now()

class Solution:
    """This class deals with solving of the problem of bipartite graph"""

    def solve(self, graph: List[List[int]],visited:List[int],current_node:int,colour:int) -> bool:
        """This function deals solving the problem of bipartite graph"""
        # Making changes in the current node and making it equal to color
        visited[current_node] = colour

        # Iterating through each and every neighbor of the graph
        for neighbour in graph[current_node]:
            # Checking if current is visited once or not
            if visited[neighbour] != -1:
                if visited[neighbour] == colour:
                    return False
            else:
                result=self.solve(graph,visited,neighbour,1-colour)
                if not result:
                    return False
        # Returning the bullion expression
        return True

    def bipartite(self)-> bool:
        """This function deals with initializing all the variables and providing data of getting the result """
        # Initializing all the variables
        graph = [[1,3], [0,2], [1,3], [0,2]]
        visited=[-1 for _ in range(len(graph))]

        # Iterating through each and every index in order to get desired output if the graph is not continuous
        for index in range(0,len(graph)):
            if visited[index] == -1:
                result = self.solve(graph,visited,index,0)
                if not result:
                    return False
        return True

#region Printing_results
end_time=datetime.now()
difference=end_time-start_time
sol = Solution()
print(sol.bipartite())
print(difference.microseconds)
#endregion
