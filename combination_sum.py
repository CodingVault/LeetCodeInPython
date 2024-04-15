#!/usr/bin/env python
# encoding: utf-8
"""
combination_sum.py

Created by Shengwei on 2014-07-20.
"""

# https://oj.leetcode.com/problems/combination-sum/
# tags: medium, array, combination, sum, dp, recursion, dfs, generator

"""
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7, 
A solution set is: 
[7] 
[2, 2, 3]
"""

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        
        def combine(nums, target, buff):
            
            for index in xrange(len(nums)):
                num = nums[index]
                if num > target:
                    break
                
                buff.append(num)
                if num == target:
                    yield list(buff)
                else:
                    for each in combine(nums[index:], target-num, buff):
                        yield each
                buff.pop()
        
        return list(combine(sorted(candidates), target, []))
