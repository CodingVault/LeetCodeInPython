#!/usr/bin/env python
# encoding: utf-8
"""
jump_game.py

Created by Shengwei on 2014-07-22.
"""

# https://oj.leetcode.com/problems/jump-game/
# tags: easy, array, greedy

"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""

# NOTE: think about how to recover the jump path

class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        cursor = farthest = 0
        
        while cursor <= farthest:
            farthest = max(farthest, cursor + A[cursor])
            if farthest >= len(A) - 1:
                return True
            cursor += 1
        
        return False
