#!/usr/bin/env python
# encoding: utf-8
"""
787. Cheapest Flights Within K Stops

Created by Shengwei on 2024-06-16.

Used:
- Snap: https://www.1point3acres.com/bbs/thread-1068337-1-1.html
"""

# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
# tags: medium, graph, Dijkstra, bfs, dfs, lowest

"""
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

 

Example 1:

Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.


Example 2:

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.


Example 3:

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
 

Constraints:

1 <= n <= 100
0 <= flights.length <= (n * (n - 1) / 2)
flights[i].length == 3
0 <= fromi, toi < n
fromi != toi
1 <= pricei <= 104
There will not be any multiple flights between two cities.
0 <= src, dst, k < n
src != dst
"""

# https://leetcode.com/problems/cheapest-flights-within-k-stops/solutions/115541/java-c-python-priority-queue-solution-tle-now/
# https://leetcode.com/problems/cheapest-flights-within-k-stops/solutions/361711/java-dfs-bfs-bellman-ford-dijkstra-s/

# Dijkstra
# Note: cannot set visited without stops; need to also double check higher prices with fewer stops
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        if src == dst: return 0
        
        import heapq

        refs = defaultdict(dict)
        for s, d, p in flights:
            refs[s][d] = p
        
        cache = [(0, src, 0)]
        visited = {}
        while cache:
            price, city, n_stop = heapq.heappop(cache)

            # note: check this outside the `for` loop
            #   as there could be multiple route to dst even in one loop
            if city == dst:
                return price

            # process it only when the # of stops to city is fewer
            if n_stop >= visited.get(city, n_stop + 1):
                continue

            if n_stop <= k:
                for c, p in refs[city].items():
                    heapq.heappush(cache, (price + p, c, n_stop + 1))

                # note: only mark city visited after outbounds are processed;
                #   there could be cases when city was reached with k+1 stops
                visited[city] = n_stop

        return -1


# TLM (20240616)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        if src == dst: return 0
        
        import heapq

        refs = defaultdict(dict)
        for s, d, p in flights:
            refs[s][d] = p
        
        cache = [(0, src, 0)]
        while cache:
            price, city, n_stop = heapq.heappop(cache)
            # print(city, price, n_stop)

            # note: check this outside the `for` loop
            #   as there could be multiple route to dst even in one loop
            if city == dst:
                return price

            if n_stop <= k:
                for c, p in refs[city].items():
                    heapq.heappush(cache, (price + p, c, n_stop + 1))
            # print(cache)

        return -1


# BFS -- Memory Limit Exceeded
from collections import defaultdict, deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src == dst: return 0

        store = defaultdict(dict)
        for s, d, p in flights:
            store[s][d] = p
        
        check = deque([(src, 0)])
        min_p = float('inf')
        stop = 0
        while check and stop <= k:
            size = len(check)
            for _ in range(size):
                place, price = check.popleft()
                for d, p in store[place].items():
                    np = price + p
                    if d == dst:
                        min_p = min(min_p, np)
                    elif np < min_p:
                        check.append((d, np))
            
            stop += 1

        return -1 if min_p == float('inf') else min_p
