#!/usr/bin/env python
# encoding: utf-8
"""
set_matrix_zeros.py

Created by Shengwei on 2014-07-06; implemented on 2014-07-27.
"""

# https://oj.leetcode.com/problems/set-matrix-zeroes/
# tags: medium / hard, matrix, in-place

"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

# https://oj.leetcode.com/discuss/1650/is-there-a-better-constant-space-solution

# Note:
#  1. it's possible to use only one variable to mark if there is 0 in the first column
#  2. there are two ways to set 0's:
#    a) go through markers and mark entire rows or columns
#    b) go through the matrix and see if it's on row or column of any marker

class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        """Stores the statistics in the first row and
        first column. Note: stores the statistics for
        the first column to the first element, and stores
        the statistics for the first row to a variable.
        """
        
        set_first_row = not all(matrix[0])
        row, col = len(matrix), len(matrix[0])
        
        # gather statistics of 0's
        for i in xrange(1, row):
            for j in xrange(col):
                if not matrix[i][j]:
                    matrix[0][j] = matrix[i][0] = 0
        
        # set 0's according to statistics
        for i in xrange(1, row):
            # Important: set rows reversely so the first
            #   column (with statistics) is set in the end
            for j in xrange(-1, -col - 1, -1):
                if not matrix[0][j] or not matrix[i][0]:
                    matrix[i][j] = 0
            
            # alternatively:
            # if not matrix[i][0]:
            #     matrix[i] = [0] * col
            #     continue
            # for j in xrange(col):
            #     if not matrix[0][j]:
            #         matrix[i][j] = 0
            
        # set the first row if necessary
        if set_first_row:
            matrix[0] = [0] * col
