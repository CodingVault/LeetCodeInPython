#!/usr/bin/env python
# encoding: utf-8
"""
permutation_ii.py

Created by Shengwei on 2014-07-15.
"""

# https://oj.leetcode.com/problems/permutations-ii/
# tags: medium / hard, numbers, permutation, dp, recursion

"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
"""

class Solution:
    # @param nums, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, nums):
        if len(nums) <= 1:
            return [nums]
        
        all_perm = []
        processed = set()
        for i in xrange(len(nums)):
            single = nums[i]
            if single in processed:
                continue
            processed.add(single)
            
            rest = nums[:i] + nums[i+1:]
            for each in self.permuteUnique(rest):
                all_perm.append(each + [single])
        
        return all_perm
