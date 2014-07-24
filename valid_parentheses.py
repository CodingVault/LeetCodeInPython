#!/usr/bin/env python
# encoding: utf-8
"""
valid_parentheses.py

Created by  on 2014-07-24.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/valid-parentheses/
# tags: easy, array, parentheses, stack

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

class Solution:
    # @return a boolean
    def isValid(self, s):
        mappings = {')': '(', ']': '[', '}': '{'}
        stack = []
        
        for par in s:
            if par in mappings.values():
                stack.append(par)
            elif stack and stack[-1] == mappings[par]:
                stack.pop()
            else:
                return False
        
        # note: remember to check if stack is empty
        return False if stack else True