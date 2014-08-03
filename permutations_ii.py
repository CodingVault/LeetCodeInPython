#!/usr/bin/env python
# encoding: utf-8
"""
permutation_ii.py

Created by  on 2014-07-15.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/permutations-ii/
# tags: medium / hard, numbers, permutation, dp, recursion

"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
"""

def perm(array):
    if len(array) <= 1:
        return [array]
    all_perm = []
    processed = set()
    for i in xrange(len(array)):
        single = array[i]
        if single in processed:
            continue
        
        processed.add(single)
        rest = array[:i] + array[i+1:]
        for each in perm(rest):
            all_perm.append(each + [single])
    return all_perm

class Solution:
    # @param nums, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, nums):
        return perm(nums)