#!/usr/bin/env python
# encoding: utf-8
"""
plus_one.py

Created by  on 2014-07-15.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/plus-one/

"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
"""

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        carry = 1
        
        for i in xrange(-1, -len(digits)-1, -1):
            digits[i] += carry
            carry, digits[i] = divmod(digits[i], 10)
            
            # Same as:
            # digits += 1
            # if digits[i] == 10:
            #     digits = 0
            # else:
            #     carry = 0
            
            if not carry:
                break
        
        if carry:
            digits.insert(0, 1)
        
        return digits