#!/usr/bin/env python
# encoding: utf-8
"""
container_with_most_water.py

Created by  on 2014-07-09.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/container-with-most-water/
# tags: medium / hard, arrays, water, greedy, logic, shortcut

"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
"""

# https://oj.leetcode.com/discuss/1074/anyone-who-has-a-o-n-algorithm

# 1. brute force
# 2. greedy algorithm
# 3. dp

class Solution:
    # @return an integer
    def maxArea(self, heights):
        start, end = 0, len(heights) - 1
        max_area = 0
        
        while start < end:
            height = min(heights[start], heights[end])
            current_area = (end - start) * height
            max_area = max(max_area, current_area)
            
            # find next pair of lines higher than current
            while start < end and heights[start] <= height:
                start += 1
            while end > start and heights[end] <= height:
                end -= 1
        
        return max_area