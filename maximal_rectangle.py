#!/usr/bin/env python
# encoding: utf-8
"""
maximal_rectangle.py

Created by  on 2014-07-05; first implemented on 2014-07-22.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/maximal-rectangle/
# tags: hard, matrix, logic, tricky, largest

"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
"""

# https://oj.leetcode.com/discuss/5198/a-o-n-2-solution-based-on-largest-rectangle-in-histogram
# http://www.geeksforgeeks.org/largest-rectangle-under-histogram/
# a variety of different algos: https://github.com/MaskRay/LeetCode/blob/master/maximal-rectangle.cc

# TODO: try different approaches

class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if len(matrix) == 0:
            return 0
        
        height = len(matrix)
        width = len(matrix[0])
        
        # consecutive 1's above one row with sentinel in the end
        ones = [0] * width + [0]
        max_area = 0
        
        for i in xrange(height):
            stack = [-1]
            # note: j goes through width+1 so it reaches sentinel
            for j in xrange(width + 1):
                if j < width and int(matrix[i][j]):
                    ones[j] += 1
                else:
                    ones[j] = 0
                
                while (len(stack) > 1 and 
                        ones[j] < ones[stack[-1]]):
                    height = ones[stack.pop()]
                    area = height * (j - stack[-1] - 1)
                    max_area = max(max_area, area)
                
                stack.append(j)
        
        return max_area
