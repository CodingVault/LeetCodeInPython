#!/usr/bin/env python
# encoding: utf-8
"""
combination_sum_ii.py

Created by  on 2014-07-20.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/combination-sum-ii/
# tags: medium, array, combination, sum, recursion, dfs

"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
A solution set is: 
[1, 7] 
[1, 2, 5] 
[2, 6] 
[1, 1, 6]
"""

# This is cheating! Directly copied from solution for combination_sum with minor edits.

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        
        def combine(nums, target, buff):
            
            for index in xrange(len(nums)):
                num = nums[index]
                if num > target:
                    break
                
                buff.append(num)
                if num == target:
                    yield tuple(buff)
                else:
                    for each in combine(nums[index+1:], target-num, buff):
                        yield each
                buff.pop()
        
        return map(list, set(combine(sorted(candidates), target, [])))
