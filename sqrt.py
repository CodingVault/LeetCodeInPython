#!/usr/bin/env python
# encoding: utf-8
"""
sqrt.py

Created by Shengwei on 2014-07-15.
"""

# https://oj.leetcode.com/problems/sqrtx/
# tags: easy / medium, numbers, search

"""
Implement int sqrt(int x).

Compute and return the square root of x.
"""

class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x < 0:
            raise ValueError('x must be a positive value.')
        if x == 0:
            return 0
        
        m = x / 2.0
        # note: using `while abs(m * m - x) > 0.0001` is
        #   not good enough for very small and very large
        #   numbers, say 1e-10 and 1e50
        while abs(m * m - x) / x > 0.0001:
            m = (m + x / m) / 2
        
        return int(m)
