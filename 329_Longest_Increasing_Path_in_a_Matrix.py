#!/usr/bin/env python
# encoding: utf-8
"""
329. Longest Increasing Path in a Matrix

Created by Shengwei on 2022-04-21.
"""

# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# tags: medium / hard, recursion, dfs, memory

"""
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).


Example 1:

Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:

Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:

Input: matrix = [[1]]
Output: 1
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
"""

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        length_matrix = [[0] * n for _ in range(m)]
        dirs = ((1, 0), (-1, 0), (0, -1), (0, 1))
        
        def get_length(i, j):
            max_distance = 1
            for d in dirs:
                ai, aj = i + d[0], j + d[1]
                if ai < 0 or ai >= m or aj < 0 or aj >= n:  # note: '>=' size
                    continue

                if matrix[ai][aj] > matrix[i][j]:
                    if length_matrix[ai][aj] == 0:
                        get_length(ai, aj)
                    max_distance = max(max_distance, 1 + length_matrix[ai][aj])

            length_matrix[i][j] = max_distance
        
        for i in range(m):
            for j in range(n):
                get_length(i, j)

        # print(length_matrix)
        return max(max(row) for row in length_matrix)
