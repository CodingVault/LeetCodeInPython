#!/usr/bin/env python
# encoding: utf-8
"""
rotate_image.py

Created by Shengwei on 2014-07-27.
"""

# https://oj.leetcode.com/problems/rotate-image/
# tags: easy / medium, matrix, rotate, spacial

"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""

# https://oj.leetcode.com/discuss/3064/in-place-solution
# TODO alternative:
#   flip horizontally, then flip diagonally (move top-left to bottom-right)
#   or, flip vertically, then flip diagonally (move bottom-left to top-right)

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)
        
        # matrix[x][y] = matrix[n-1-y][x]
        for i in xrange(n / 2):
            for j in xrange(i, n - i - 1):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-i-1] = tmp
        
        return matrix
