#!/usr/bin/env python
# encoding: utf-8
"""
permutations.py

Created by Shengwei on 2014-07-15.
"""

# https://oj.leetcode.com/problems/permutations/
# tags: medium, numbers, permutation, dp, recursion, generator

"""
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
"""

# 20240413 -- generator
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def perm(array):
            if len(array) <= 1:
                yield array
                # alternatively, `return` here directly
            
            else:
                for i, cur in enumerate(array):
                    rest = array[:i] + array[i+1:]
                    for each in perm(rest):
                        yield each + [cur]
        
        return list(perm(nums))



class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, nums):

        def perm(array):
            if len(array) <= 1:
                return [array]
            all_perm = []
            for i in xrange(len(array)):
                single = array[i]
                rest = array[:i] + array[i+1:]
                for each in perm(rest):
                    all_perm.append(each + [single])
            return all_perm
        
        return perm(nums)
