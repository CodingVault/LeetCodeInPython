#!/usr/bin/env python
# encoding: utf-8
"""
subsets_ii.py

Created by Shengwei on 2014-07-20.
"""

# https://oj.leetcode.com/problems/subsets-ii/
# tags: easy / medium, numbers, set, combination, dfs

"""
Given a collection of integers that might contain duplicates, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

# TODO: different ways to do it

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        result = [[]]
        
        pre_num = min(S) - 1
        for num in sorted(S):
            # note: end must have been assigned
            # for pre_num when num == pre_num
            start = 0 if num != pre_num else end
            end = len(result)
            for sub_set in result[start:end]:
                result.append(sub_set + [num])
            pre_num = num
        
        return result
