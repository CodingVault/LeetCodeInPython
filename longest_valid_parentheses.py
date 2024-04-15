#!/usr/bin/env python
# encoding: utf-8
"""
longest_valid_parentheses.py

Created by Shengwei on 2014-07-08.
"""

# https://oj.leetcode.com/problems/longest-valid-parentheses/
# tags: medium / hard, array, parentheses, stack, longest

"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""

# alternative: D&C

class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        stack = []
        
        # for '(' at given index, store the length of matching pair ')';
        # the last one length[len(s)] is a sentinel
        lengths = [0] * (len(s) + 1)
        
        # alternative: `for i, chr in enumerate(s):`
        for i in xrange(len(s)):
            if s[i] == '(':
                stack.append(i)
            if s[i] == ')':
                if stack:
                    left_index = stack.pop()
                    lengths[left_index] = i + 1 - left_index
        
        max_length = current_length = i = 0
        while i < len(s):
            current_length = lengths[i]
            
            # for the last pair, i + current_length == len(s), and
            # it takes advantage of the sentinel
            while lengths[i + current_length] > 0:
                current_length += lengths[i + current_length]
            
            max_length = max(max_length, current_length)
            i += current_length + 1
        
        return max_length
