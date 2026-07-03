from typing import List
import sys
import heapq

class Solution:
    """This class deals with application of the algorithm for finding the shortest distance between two nodes"""

    def solve(self,adj_list:List[List[int]],dis:List[int],src:int) -> None:
        # Making the distance of the self node equal to zero
        dis[src]=0

        # Initializing the priority queue
        queue=[[0,src]]

        while queue:
            current_dis,node=heapq.heappop(queue)

            if current_dis != dis[node]:
                continue

            for adjNode,weight in adj_list[node]:
                distance_travel= current_dis + weight

                if distance_travel < dis[adjNode]:
                    dis[adjNode]=distance_travel
                    heapq.heappush(queue,[distance_travel,adjNode])

    def dijkstra(self) -> List[int]:
        """This function defines all the variables required for the algorithm"""
        # Defining of the variables
        nodes = 5
        src = 0
        edges = [
            (0, 1, 4), (0, 2, 1),
            (2, 1, 2), (1, 3, 1),
            (2, 3, 5), (3, 4, 3)
        ]

        # Making empty list of adjacency for number of nodes
        adj_list=[[] for _ in range(nodes)]

        # Formation of the adjacency list
        for u,v,d in edges:
            adj_list[u].append([v,d])

        # Making the distance list
        distance=[sys.maxsize for _ in range(nodes)]

        # Calling the soon solve function in order to get the distance in the list
        self.solve(adj_list,distance,src)
        return distance

sol = Solution()
print(sol.dijkstra())