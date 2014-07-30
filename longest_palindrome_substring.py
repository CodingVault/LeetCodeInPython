#!/usr/bin/env python
# encoding: utf-8
"""
longest_palindrome_substring.py

Created by  on 2014-07-16.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/longest-palindromic-substring/

"""
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
"""

############# O(n) #############
# TODO

############# O(n^2) #############

class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if s is None or len(s) == 0:
            return ''
        
        max_palin = s[0]
        for i in xrange(1, len(s)):
            
            def get_max(left, cur_s, right, max_palin):
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    cur_s = s[left] + cur_s + s[right]
                    left -= 1
                    right += 1
                
                return cur_s if len(cur_s) > len(max_palin) else max_palin
            
            # even palindrome
            max_palin = get_max(i - 1, '', i, max_palin)
            
            # odd palindrome
            max_palin = get_max(i - 1, s[i], i + 1, max_palin)
        
        return max_palin
            
