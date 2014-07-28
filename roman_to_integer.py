#!/usr/bin/env python
# encoding: utf-8
"""
roman_to_integer.py

Created by  on 2014-07-27.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/roman-to-integer/
# tags: easy, numbers, roman, convert

"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""

# https://oj.leetcode.com/discuss/2369/solution-for-this-question-but-dont-know-there-any-easier-way

class Solution:
    # @return an integer
    def romanToInt(self, s):
        roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = pre = 0
        
        for c in reversed(s):
            cur = roman_dict[c]
            if cur >= pre:
                result += cur
            else:
                result -= cur
            pre = cur
        
        return result
