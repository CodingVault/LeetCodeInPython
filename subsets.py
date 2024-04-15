#!/usr/bin/env python
# encoding: utf-8
"""
subsets.py

Created by Shengwei on 2014-07-20.
"""

# https://oj.leetcode.com/problems/subsets/
# tags: easy / medium, numbers, set, combination, dfs, generator

"""
Given a set of distinct integers, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

# TODO: different ways to do it


# 20240415 - generator
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def gen(array):
            if not array:
                yield []
                return
            
            for subset in gen(array[1:]):
                yield subset
                yield [array[0]] + subset
        
        return list(gen(nums))




class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        result = [[]]
        
        for num in sorted(S):
            cur_len = len(result)
            for sub_set in result[:cur_len]:
                result.append(sub_set + [num])
        
        return result


######### DFS #########

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        
        def dfs(sub_set, buff):
            result = [buff]
            for index in xrange(len(sub_set)):
                cur_buff = list(buff) + [sub_set[index]]
                result.extend(dfs(sub_set[index+1:], cur_buff))
            
            return result
        
        return dfs(sorted(S), [])
