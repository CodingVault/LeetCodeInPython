#!/usr/bin/env python
# encoding: utf-8
"""
spiral_matrix.py

Created by  on 2014-07-27.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/spiral-matrix/
# tags: medium / hard, matrix, spacial, edge cases

"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""

# https://oj.leetcode.com/discuss/3925/1-2-4-3-is-not-a-wrong-answer
# alternatives that don't work (m rows and n cols):
#   1. [0][0,n-2,1] + [0,m-2,1][n-1] + [m-1][n-1,1,-1] + [m-1,1,-1][0]
#       It will not process the very center one (think m == n == 1).
#   2. [0][0,n-1,1] + [1,m-2,1][n-1] and [m-1][n-1,0,-1] + [m-2,1,-1][0]
#       When m == 1 and n >= 1, it will process the line twice.

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        """ -------->
            ^       |
            |       |
            |       |
            <-------V
        """
        if len(matrix) == 0:
            return []
        
        top, right, bottom, left = 0, 1, 2, 3
        
        def generator():
            row_start, row_end = 0, len(matrix) - 1
            col_start, col_end = 0, len(matrix[0]) - 1
            i = j = 0
            processing = 0
            
            while row_start <= row_end and col_start <= col_end:
                # note: need to check the (partial) condition before
                #   processing each line
                
                if processing == top:
                    # left -> right
                    for j in xrange(col_start, col_end + 1):
                        yield matrix[i][j]
                    # visited row_start, increase it; j == col_end
                    row_start += 1
                
                elif processing == right:
                    # top -> down
                    for i in xrange(row_start, row_end + 1):
                        yield matrix[i][j]
                    # visited col_end, decrease it; i == row_end
                    col_end -= 1
                
                elif processing == bottom:
                    # right -> left
                    for j in xrange(col_end, col_start - 1, -1):
                        yield matrix[i][j]
                    # visited row_end, decrease it; j == col_start
                    row_end -= 1
                
                else:
                    # processing == left; bottom -> top
                    for i in xrange(row_end, row_start - 1, -1):
                        yield matrix[i][j]
                    # visited col_start, increase it; i == row_end
                    col_start += 1
                
                processing = (processing + 1) % 4
        
        return list(generator())
