#!/usr/bin/env python
# encoding: utf-8
"""
unique_path.py

Created by Shengwei on 2014-07-28.
"""

# https://oj.leetcode.com/problems/unique-paths/
# tags: easy / medium, matrix, path, dp

"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.
"""

# https://oj.leetcode.com/discuss/383/solve-unique-paths-with-linear-algorithm

# Improvoment: only need O(min(m,n)) space

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        matrix = [[0] * n for _ in range(m - 1)]
        # note: this init needs to be outside of the loop
        matrix.append([1] * n)
        
        for i in range(-2, -m - 1, -1):
            for j in range(-1, -n - 1, -1):
                down = right = 0
                if i + 1 < 0:
                    down = matrix[i + 1][j]
                if j + 1 < 0:
                    right = matrix[i][j + 1]
                matrix[i][j] = down + right
        
        return matrix[0][0]
