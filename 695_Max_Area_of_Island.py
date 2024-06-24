#!/usr/bin/env python
# encoding: utf-8
"""
695. Max Area of Island

Created by Shengwei on 2024-06-23.

Used:
- Snap: https://www.1point3acres.com/bbs/thread-1061851-1-1.html
"""

# https://leetcode.com/problems/max-area-of-island/description/
# tags: medium, matrix, bfs, dfs, area

"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.


Example 1:

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.


Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
"""


# bfs
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0

        m, n = len(grid), len(grid[0])
        visited = set()

        def get_area(x, y):
            directions = (0, 1, 0, -1, 0)
            visited.add((x, y))
            buffer = deque([(x, y)])  # any pos put in buffer are not in visited
            area = 0
            while buffer:
                i, j = buffer.popleft()
                area += 1
                
                for di, dj in zip(directions, directions[1:]):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] and (ni, nj) not in visited:
                    	# note: must update `visited` within the loop
                        visited.add((ni, nj))
                        buffer.append((ni, nj))

            return area

        max_area = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] and (x, y) not in visited:
                    max_area = max(max_area, get_area(x, y))
        return max_area


# dfs
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0

        m, n = len(grid), len(grid[0])
        visited = set()

        def dfs(x, y):
            directions = (0, 1, 0, -1, 0)
            if 0 <= x < m and 0 <= y < n and grid[x][y] and (x, y) not in visited:
                area = 1
                visited.add((x, y))
                for dx, dy in zip(directions, directions[1:]):
                    area += dfs(x + dx, y + dy)
                return area
            return 0
        
        max_area = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] and (x, y) not in visited:
                    max_area = max(max_area, dfs(x, y))
        return max_area
