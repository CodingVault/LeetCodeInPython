#!/usr/bin/env python
# encoding: utf-8
"""
spiral_matrix_ii.py

Created by  on 2014-07-27.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/spiral-matrix-ii/
# tags: medium / hard, matrix, spacial, edge cases

"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        """ -------->
            ^       |
            |       |
            |       |
            <-------V
        """
        matrix = [[0] * n for _ in range(n)]
        num = 1
        i = j = 0
        
        for start in xrange((n + 1) / 2):
            for j in xrange(start, n - start):
                matrix[i][j] = num
                num += 1
            for i in xrange(start + 1, n - start):
                matrix[i][j] = num
                num += 1
            for j in xrange(n - start - 2, start - 1, -1):
                matrix[i][j] = num
                num += 1
            for i in xrange(n - start - 2, start, -1):
                matrix[i][j] = num
                num += 1
        
        return matrix
