#!/usr/bin/env python
# encoding: utf-8
"""
word_break.py

Created by Shengwei on 2014-07-01.
"""

# https://oj.leetcode.com/problems/word-break/
# tags: easy / medium, string, dp, cached

"""
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""

# better: store mappings with keys as indices other than strings

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        string_with_words = {'': True}
    
        def can_break_string(s):
            if s in string_with_words:
                return string_with_words[s]
            
            for index in xrange(len(s)):
                remainder = s[index+1:]
                if s[:index+1] in dict and can_break_string(remainder):
                    string_with_words[s] = True
                    return True
            
            string_with_words[s] = False
            return False
        
        return can_break_string(s)



