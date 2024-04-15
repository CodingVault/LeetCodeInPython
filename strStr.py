#!/usr/bin/env python
# encoding: utf-8
"""
strStr.py

Created by Shengwei on 2014-07-28.
"""

# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
# https://oj.leetcode.com/problems/implement-strstr/
# tags: medium / hard, string, matching

"""
Implement strStr().

Returns a pointer to the first occurrence of needle in haystack, or null if needle is not part of haystack.
"""

# https://oj.leetcode.com/discuss/1159/are-we-expected-to-use-kmp-for-this-problem
# http://leetcode.com/2010/10/implement-strstr-to-find-substring-in.html
# https://gist.github.com/senvey/b602a0fc7ef39daf4b41


# 20180502
class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        
        # note: when the first char doesn't match, needle
        #   needs to move forward, so table[0] must be -1;
        #   when the second char doesn't match, it must 
        #   start with the first char, so table[1] must be 0
        table = [-1]
        i, j = 0, -1
        while i < len(needle):
            if j == -1 or needle[i] == needle[j]:
                # no match whatsoever, or found a match
                # for needle[i] at index j, update table:
                # table[i + 1] == j + 1;
                # move forward to process next i
                i += 1
                j += 1
                table.append(j)
            else:
                j = table[j]
        
        i = j = 0
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = table[j]
        
        if j == len(needle):
            return i - j
        
        return -1


# 20140728
class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        
        # note: when the first char doesn't match, needle
        #   needs to move forward, so table[0] must be -1;
        #   when the second char doesn't match, it must 
        #   start with the first char, so table[1] must be 0
        table = [-1]
        i, j = 0, -1
        while i < len(needle):
            if j == -1 or needle[i] == needle[j]:
                # no match whatsoever, or found a match
                # for needle[i] at index j, update table:
                # table[i + 1] == j + 1;
                # move forward to process next i
                i += 1
                j += 1
                table.append(j)
            else:
                j = table[j]
        
        i = j = 0
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = table[j]
        
        if j == len(needle):
            return haystack[i - j:]
        
        return None
