#!/usr/bin/env python
# encoding: utf-8
"""
add_binary.py

Created by Shengwei on 2014-07-15.
"""

# https://oj.leetcode.com/problems/add-binary/

"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        if not a or not b:
            return a or b
        
        index = -1
        carry = 0
        result = []
        while -index <= max(len(a), len(b)):
            x = int(a[index]) if -index <= len(a) else 0
            y = int(b[index]) if -index <= len(b) else 0
            carry, remainder = divmod(x + y + carry, 2)
            result.append(remainder)
            index -= 1
        
        if carry:
            result.append(carry)
        
        return ''.join(map(str, reversed(result)))
