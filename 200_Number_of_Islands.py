#!/usr/bin/env python
# encoding: utf-8
"""
200. Number of Islands

Created by Shengwei on 2025-05-08.

Used:
- TikTok: https://www.1point3acres.com/bbs/thread-1064304-1-1.html
- Disney: https://www.1point3acres.com/bbs/thread-1067063-1-1.html
"""

# https://leetcode.com/problems/number-of-islands/description/
# tags: medium, matrix, bfs, dfs

"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""


# 20240603
from collections import deque

def num_of_islands(matrix):
    if not matrix or not matrix[0]:
        return 0

    m, n = len(matrix), len(matrix[0])
    visited = [[0] * n for _ in range(m)]
    count = 0

    def valid(i, j):
        return 0 <= i < m and 0 <= j < n

    def identify(i, j):

        def process(x, y):
            if valid(x, y) and not visited[x][y]:
                if matrix[x][y] == '1':
                    queue.append((x, y))

        queue = deque([(i, j)])
        while queue:
            ci, cj = queue.popleft()
            visited[ci][cj] = 1
            process(ci + 1, cj)
            process(ci - 1, cj)
            process(ci, cj + 1)
            process(ci, cj - 1)


    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1' and not visited[i][j]:
                identify(i, j)
                count += 1

    return count

# alternative
def num_of_islands(matrix):
    if not matrix or not matrix[0]:
        return 0

    m, n = len(matrix), len(matrix[0])
    visited = [[0] * n for _ in range(m)]

    def valid(i, j):
        return 0 <= i < m and 0 <= j < n

    def identify(i, j):

        def process(x, y):
            if valid(x, y) and not visited[x][y]:
                if matrix[x][y] == '1':
                    queue.append((x, y))

        queue = deque([(i, j)])
        while queue:
            ci, cj = queue.popleft()
            visited[ci][cj] = 1
            process(ci + 1, cj)
            process(ci - 1, cj)
            process(ci, cj + 1)
            process(ci, cj - 1)

        return 1

    return sum(identify(i, j) 
        for i in range(m) 
        for j in range(n) 
        if matrix[i][j] == '1' and not visited[i][j]
    )
