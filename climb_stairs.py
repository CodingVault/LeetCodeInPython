#!/usr/bin/env python
# encoding: utf-8
"""
climb_stairs.py

Created by Shengwei on 2014-07-06.
"""

# https://oj.leetcode.com/problems/climbing-stairs/
# tags: medium, numbers, dp, recursion

"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

# TODO: different ways to do this



# 20240329
def climb(n):
    if n <= 2:
        return n

    prior, cur = 1, 2
    for _ in range(n - 2):
        prior, cur = cur, prior + cur
    return cur



class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        ways = [1, 1]
        
        def subroutine(n):
            if n >= len(ways) and n >= 2:
                ways.append(subroutine(n - 1) + subroutine(n - 2))
                
            return ways[n]
            
        return subroutine(n)
