#!/usr/bin/env python
# encoding: utf-8
"""
word_break_ii.py

Created by Shengwei on 2014-07-01.
"""

# https://oj.leetcode.com/problems/word-break-ii/
# tags: medium, string, dp, cached

"""
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
"""

# https://oj.leetcode.com/discuss/133/is-there-better-solution-for-this-word-breakii
# 1. build a dict of all valid word found in the string
#   note: only store indices which can be connected word by word
# 2. collect words from start to each stop of one word

# better: store mappings with keys as indices other than strings

class Solution:
    # @param s, a string
    # @param dictionary, a set of string
    # @return a list of strings
    def wordBreak(self, s, dictionary):
        string_with_words = collections.defaultdict(list)
        
        def break_string(s):
            if s in string_with_words:
                return string_with_words[s]
            
            res = string_with_words[s]
            if s in dictionary:
                res.append(s)
            
            for index in xrange(len(s)):
                cut = s[:index+1]
                if cut in dictionary:
                    for words in break_string(s[index+1:]):
                        res.append(cut + ' ' + words)
            
            return res
        
        return break_string(s)
