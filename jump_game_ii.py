#!/usr/bin/env python
# encoding: utf-8
"""
jump_game_ii.py

Created by  on 2014-07-22.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/jump-game-ii/
# tags: medium, array, dp, greedy, logic

"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
"""

# https://oj.leetcode.com/discuss/422/is-there-better-solution-for-jump-game-ii


################# adding some logic O(n) #################

class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        # note: this needs special care
        if len(A) == 1:
            return 0
        
        step = farthest = 0
        next_farthest = A[0]
        
        for cursor in xrange(len(A) - 1):
            can_reach = cursor + A[cursor]
            if can_reach >= len(A) - 1:
                return step + 1
            
            next_farthest = max(next_farthest, can_reach)
            
            if cursor == farthest:
                if farthest == next_farthest:
                    # this is the farthest position it
                    # can reach; cannot reach the final
                    break
                
                # it needs one more step to reach further
                # since next potion, i.e., farthest + 1
                step += 1
                farthest = next_farthest
        
        # cannot reach the last index
        return 1000000


################# bottom-up dp O(n^2) #################

class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        steps = [0] + [100000] * (len(A) - 1)
        
        for i in xrange(len(A) - 1):
            for cursor in xrange(i + 1, i + A[i] + 1):
                if cursor >= len(A):
                    break
                steps[cursor] = min(
                    steps[cursor], steps[i] + 1)
        
        return steps[-1]