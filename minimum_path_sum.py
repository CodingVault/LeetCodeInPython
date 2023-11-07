#!/usr/bin/env python
# encoding: utf-8
"""
minimum_path_sum.py

Created by Shengwei on 2014-07-28.
"""

# https://oj.leetcode.com/problems/minimum-path-sum/
# tags: easy / medium, matrix, path, sum, dp

"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""

# Improvoment: only need O(min(m,n)) space

class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        matrix = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    matrix[0][0] = grid[0][0]
                    continue
                
                up = left = 1000000
                if i - 1 >= 0:
                    up = matrix[i - 1][j]
                if j - 1 >= 0:
                    left = matrix[i][j - 1]
                matrix[i][j] = min(up, left) + grid[i][j]
        
        return matrix[-1][-1]
