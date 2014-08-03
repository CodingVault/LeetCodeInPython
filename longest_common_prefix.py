#!/usr/bin/env python
# encoding: utf-8
"""
longest_common_prefix.py

Created by Shengwei on 2014-07-15.
"""

# https://oj.leetcode.com/problems/longest-common-prefix/
# tags: easy / medium, array, string, pointer, logest, D&C, edge cases

"""
Write a function to find the longest common prefix string amongst an array of strings.
"""

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        
        for index in xrange(len(strs[0])):
            char = strs[0][index]
            for s in strs:
                if index >= len(s) or char != s[index]:
                    return strs[0][:index]
        
        return strs[0]


############### D&C ###############

class Solution:
    # @return a string
    def longestCommonPrefix(self, array):
        if array is None or len(array) == 0:
            return ''

        if len(array) == 1:
            return array[0]

        half = len(array) / 2
        longest_left = self.longestCommonPrefix(array[:half])
        longest_right = self.longestCommonPrefix(array[half:])

        min_length = min(len(longest_left), len(longest_right))
        for index in xrange(min_length):
            if longest_left[index] != longest_right[index]:
                return longest_left[:index]

        return longest_left[:min_length]
