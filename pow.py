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

# https://leetcode.com/problems/powx-n/discuss/19560/Shortest-Python-Guaranteed

# TODO: try bit manipulation


# Solution 1
class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n < 0:
            return 1.0 / recursive_pow(x, -n)
        return recursive_pow(x, n)

    @staticmethod
    def recursive_pow(x, n):
        if n == 0: return 1
        if n == 1: return x
        half, rest = divmod(n, 2)
        product = recursive_pow(x, half)
        if rest == 0:
            return product * product
        return product * product * x


# Solution 2
def pow(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1.0 / pow(x, -n)

    res = 1
    while n:
        if n % 2 == 1:
            # x keeps tracking power of 2 to this point;
            # for pow(pow(pow(x, 2) * x, 2), 2), when it reaches the most inner pow(x, 2), x = pow(pow(x, 2), 2)
            res *= x
        x *= x
        n >>= 1
    return res