#!/usr/bin/env python
# encoding: utf-8
"""
single_number_ii.py

Created by Shengwei on 2014-07-23.
"""

# https://oj.leetcode.com/problems/single-number-ii/
# tags: medium / hard, numbers, logic, tricky

"""
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

# https://oj.leetcode.com/discuss/857/constant-space-solution
# https://oj.leetcode.com/discuss/5122/how-does-python-work-on-bits
# TODO: try different approaches
# note: two loops from 0 through 31 can be combined

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        count = [0] * 32
        
        for number in A:
            for i in xrange(32):
                count[i] += number >> i & 1
        
        result = 0
        for i in xrange(32):
            result |= count[i] % 3 << i
        
        # Python needs special treatment for negative values
        if count[-1] % 3 == 1:
            # manually revert the thing: -i = (~i) + 1
            result = -(result - 1 ^ (1 << 32) - 1)
        
        return result
