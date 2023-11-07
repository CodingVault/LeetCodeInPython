#!/usr/bin/env python
# encoding: utf-8
"""
unique_path_ii.py

Created by Shengwei on 2014-07-28.
"""

# https://oj.leetcode.com/problems/unique-paths-ii/
# tags: medium, matrix, path, dp

"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
"""

# Improvoment: only need O(min(m,n)) space

class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        matrix = [[0] * n for _ in range(m - 1)]
        last_row = [0] * n
        for index in range(-1, -n - 1, -1):
            if obstacleGrid[-1][index]:
                break
            last_row[index] = 1
        matrix.append(last_row)
        
        for i in range(-2, -m - 1, -1):
            for j in range(-1, -n - 1, -1):
                if obstacleGrid[i][j]:
                    continue
                
                down = right = 0
                if i + 1 < 0:
                    down = matrix[i + 1][j]
                if j + 1 < 0:
                    right = matrix[i][j + 1]
                matrix[i][j] = down + right
        
        return matrix[0][0]
