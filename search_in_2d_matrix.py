#!/usr/bin/env python
# encoding: utf-8
"""
search_in_2d_matrix.py

Created by  on 2014-07-24.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/search-a-2d-matrix/
# tags: easy / medium, matrix, search, edge cases

"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
"""

# https://oj.leetcode.com/discuss/6201/compare-some-of-solutions-witch-is-most-effective

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        
        # look for the row where target locates
        up, down = 0, len(matrix)
        while up < down:
            mid = (up + down) / 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] > target:
                down = mid
            else:
                up = mid + 1
        
        # up == down == i+1 where target is in
        # row i if it exists; i.e.,
        # matrix[up][0] > target > matrix[up-1][0]
        if up == 0:
            return False
        row = up - 1
        
        # search in the row
        left, right = 0, len(matrix[row])
        while left < right:
            mid = (left + right) / 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] > target:
                right = mid
            else:
                left = mid + 1
        
        return False
