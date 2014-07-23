#!/usr/bin/env python
# encoding: utf-8
"""
trap_rain_water.py

Created by  on 2014-07-22.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/trapping-rain-water/
# tags: medium / hard, array, water, greedy, logic, tricky, edge cases

"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

[image]
"""

# https://oj.leetcode.com/discuss/3546/any-one-pass-solutions

# TODO: convert if statement to while loop for shortcut

class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        if len(A) <= 1:
            return 0
        
        left, right = 0, len(A) - 1
        total = height = 0
        
        while left <= right:
            height = max(height, min(A[left], A[right]))
            total += height
            
            if A[left] < A[right]:
                left += 1
            else:
                right -= 1
        
        return total - sum(A)