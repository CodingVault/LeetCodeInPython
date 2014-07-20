#!/usr/bin/env python
# encoding: utf-8
"""
longest_string_without_repeating_chars.py

Created by  on 2014-07-09.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/longest-substring-without-repeating-characters/

"""
Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
"""

# http://leetcode.com/2011/05/longest-substring-without-repeating-characters.html
# https://oj.leetcode.com/discuss/6168/my-o-n-solution

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        cache = set()
        start = end = 0
        max_length = 0
        
        while end < len(s):
            
            # BAD! actually this can be re-written using if statement
            
            # note: need to check if end < len(s) here
            while end < len(s) and s[end] not in cache:
                cache.add(s[end])
                end += 1
            
            max_length = max(max_length, end - start)
            
            # note: break the loop after updating max_length
            if end == len(s):
                break
            
            while s[start] != s[end]:
                cache.remove(s[start])
                start += 1
            # note: remember to remove the last s[start]
            cache.remove(s[start])
            start += 1
        
        return max_length

# alternative: use dict instead of set to shortcut the second inner loop

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        cache = {}
        start = end = 0
        max_length = 0

        while end < len(s):
            if s[end] in cache and cache[s[end]] >= start:
                # the char s[end] exists in range [start, end),
                # move start to the next char of prior `s[end]`
                start = cache[s[end]] + 1

            # update the index with latest one
            cache[s[end]] = end
            end += 1

            max_length = max(max_length, end - start)

        return max_length