#!/usr/bin/env python
# encoding: utf-8
"""
2sum.py

Created by Shengwei on 2014-07-15.
"""

# https://oj.leetcode.com/problems/two-sum/
# tags: easy / medium, numbers, search

"""
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        snum = sorted(num)
        i, j = 0, -1
        while i - j < len(num):
            if snum[i] + snum[j] == target:
                index1 = num.index(snum[i]) + 1
                if snum[i] != snum[j]:
                    index2 = num.index(snum[j]) + 1
                else:
                    index2 = num.index(snum[j], index1) + 1
                    
                if index1 < index2:
                    return index1, index2
                return index2, index1
            if snum[i] + snum[j] < target:
                i += 1
            else:
                j -= 1
