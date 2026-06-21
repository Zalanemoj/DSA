# importing libraries
from collections import deque
from typing import List

class BreathFirstSearch:
    """Class that deals with the breath first search"""

    def solve(self,no_nodes:int , visited_nodes:list , adjacency_list:list, result:list,starting_node:int) -> None:
        """Return a traversal of the nodes as per depth first search"""
        queue=deque()
        queue.append(starting_node)
        visited_nodes[starting_node]=1
        #  The loop should run until stack does not get empty
        while queue:
            e=queue.popleft()
            result.append(e)
            # Iterating through the adjacency list in order to get the neighbor of a particular node
            for neighbor in adjacency_list[e]:
                # If a particular note is visited then we don't need to add it in the stack
                if not visited_nodes[neighbor]:
                    queue.append(neighbor)
                    visited_nodes[neighbor]=1


    def bfs(self) -> List[int]:
        """It is kind of a calling function for breath first search"""
        # Initializing all the variables that are required
        no_nodes=9
        adjacency_list=[[], [2, 3], [1, 4], [4, 1, 5], [2, 3, 5], [3, 4]]
        result=[]
        visited_nodes=[0]*(no_nodes+1)
        # Calling of the function
        self.solve(no_nodes,visited_nodes,adjacency_list,result,1)
        # Returning the result in a list of integer format
        return result

#region Printing
sol=BreathFirstSearch()
print(sol.bfs())
#endregion

# Time Complexity -> o(n) + o(2*Number of edges )
# Space Complexity -> o(n)