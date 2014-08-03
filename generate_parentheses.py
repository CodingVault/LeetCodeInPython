#!/usr/bin/env python
# encoding: utf-8
"""
generate_parentheses.py

Created by Shengwei on 2014-07-28.
"""

# https://oj.leetcode.com/problems/generate-parentheses/
# tags: medium, generator, parentheses, dfs, recursion, dp

"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
"""

# CC 8.5

class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        
        def generator(s, left, right):
            if left == 0 and right == 0:
                yield s
            
            if left > 0:
                for each in generator(s + '(', left - 1, right):
                    yield each
            
            if right > left:
                for each in generator(s + ')', left, right - 1):
                    yield each
        
        return list(generator('', n, n))
