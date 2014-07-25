#!/usr/bin/env python
# encoding: utf-8
"""
sqrt.py

Created by  on 2014-07-15.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
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
        while abs(m * m - x) > 0.000001:
            m = (m + x / m) / 2
        
        return int(m)