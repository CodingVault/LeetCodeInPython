#!/usr/bin/env python
# encoding: utf-8
"""
longest_common_prefix.py

Created by  on 2014-07-15.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/longest-common-prefix/

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