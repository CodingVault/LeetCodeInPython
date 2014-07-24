#!/usr/bin/env python
# encoding: utf-8
"""
remove_element.py

Created by  on 2014-07-15.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/remove-element/
# tags: easy, array, pointer

"""
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if A is None or len(A) == 0:
            return 0
        
        cursor = 0
        pos = 0
        while cursor < len(A):
            if A[cursor] != elem:
                A[pos] = A[cursor]
                pos += 1
            cursor += 1
        return pos