#!/usr/bin/env python
# encoding: utf-8
"""
simplify_path.py

Created by Shengwei on 2014-07-24.
"""

# https://oj.leetcode.com/problems/simplify-path/
# tags: easy, array, stack, edge cases
# edge cases: '/../', '/', '/foo///bar/'

"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
"""

class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        staging = path.split('/')
        stack = ['']
        
        for sec in staging:
            if sec == '' or sec == '.':
                pass
            elif sec == '..':
                if len(stack) > 1:
                    stack.pop()
            else:
                stack.append(sec)
        
        # note: remember to handle the edge case
        if len(stack) == 1:
             return '/'
        return '/'.join(stack)
