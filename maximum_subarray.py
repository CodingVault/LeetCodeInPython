#!/usr/bin/env python
# encoding: utf-8
"""
maximum_subarray.py

Created by  on 2014-07-22.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/maximum-subarray/
# tags: medium, array, optimization, D&C, dp

"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

# http://en.wikipedia.org/wiki/Maximum_subarray_problem
# TODO: try different approach (see also Programming Pearls)

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        
        # in case there is only negative numbers, it should:
        #   1. init max_sum with -sys.maxint-1
        #   2. update sum_to_cursor with `max(sum_to_cursor, 0) + num`
        #       instead of `max(sum_to_cursor + num, 0)`
        max_sum = -1000000
        sum_to_cursor = 0
        
        for num in A:
            sum_to_cursor = max(sum_to_cursor, 0) + num
            max_sum = max(max_sum, sum_to_cursor)
        
        return max_sum
