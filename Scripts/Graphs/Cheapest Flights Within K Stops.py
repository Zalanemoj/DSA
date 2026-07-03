import sys
from collections import deque
from typing import List


class Solution:
    def findcheapestprice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = [[] for _ in range(n)]

        for u, v, c in flights:
            adj_list[u].append([v, c])

        min_cost = [sys.maxsize for _ in range(n)]
        min_cost[src] = 0

        queue = deque()
        queue.append([0, src, 0])

        while queue:
            stop, node, cost = queue.popleft()

            for next, price in adj_list[node]:
                new_cost = cost + price
                new_stop = stop + 1

                if new_stop == k + 1 and next != dst:
                    continue

                if new_cost < min_cost[next]:
                    min_cost[next] = new_cost
                    queue.append([new_stop, next, new_cost])

        return -1 if min_cost[dst] == sys.maxsize else min_cost[dst]
