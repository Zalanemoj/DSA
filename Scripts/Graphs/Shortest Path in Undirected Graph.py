# importing Libraries
from typing import List
from collections import deque

class Solution:
    """This Class deals solving the problem of Shortest path in an undirected graph"""

    def solve(self,adj:List[List[int]],distance:List[int],src:int,nodes:int)->None:
        distance[src]=0

        queue=deque()
        queue.append(src)

        while queue:
            node=queue.popleft()
            for neighbour in adj[node]:
                if distance[neighbour]==-1:
                    distance[neighbour]=distance[node]+1
                    queue.append(neighbour)


    def shortest_path(self) -> List[int]:
        """This function deals with initialization of all the variables required for solving the problem"""

        nodes=6
        edges=[[0,1],[0,2],[1,3],[2,3],[3,4]]
        distance=[-1]*nodes
        adj_list = [[] for _ in range(nodes)]
        src=0

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        for _ in range(nodes):
            self.solve(adj_list,distance,src,nodes)

        return distance

sol=Solution()
print(sol.shortest_path())