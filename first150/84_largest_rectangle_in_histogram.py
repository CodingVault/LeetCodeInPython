#!/usr/bin/env python
# encoding: utf-8
"""
largest_rectangle_in_histogram.py

Created by Shengwei on 2014-07-05; first implemented on 2014-07-22.
"""

# https://oj.leetcode.com/problems/largest-rectangle-in-histogram/
# tags: hard, array, stack, largest, logic, tricky, D&C, edge cases

"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

[image]
Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

[image]
The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10.
"""

# D & C: http://www.geeksforgeeks.org/largest-rectangular-area-in-a-histogram-set-1/
# Linear: http://www.geeksforgeeks.org/largest-rectangle-under-histogram/

class Solution:
    # @param heights, a list of integer
    # @return an integer
    def largestRectangleArea(self, heights):
        stack = [-1]   # sentinel
        max_area = 0
        heights.append(0)   # sentinel
        
        for index in xrange(len(heights)):
            while len(stack) > 1 and heights[index] < heights[stack[-1]]:
                height = heights[stack.pop()]
                area = height * (index - stack[-1] - 1)
                max_area = max(max_area, area)
            
            stack.append(index)
        
        # reset heights back as the input
        heights.pop()
        return max_area
