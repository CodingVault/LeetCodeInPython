#!/usr/bin/env python
# encoding: utf-8
"""
climb_stairs.py

Created by  on 2014-07-06.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/climbing-stairs/

"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

# TODO: different ways to do this

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