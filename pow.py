#!/usr/bin/env python
# encoding: utf-8
"""
pow.py

Created by Shengwei on 2014-07-15.
"""

# https://oj.leetcode.com/problems/powx-n/
# tags: easy / medium, numbers, D&C, bit manipulation

"""
Implement pow(x, n).
"""

# TODO: try bit manipulation

def recursive_pow(x, n):
    if n == 0: return 1
    if n == 1: return x
    half, rest = divmod(n, 2)
    product = recursive_pow(x, half)
    if rest == 0:
        return product * product
    return product * product * x
    

class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n < 0:
            return 1.0 / recursive_pow(x, -n)
        return recursive_pow(x, n)
