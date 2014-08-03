#!/usr/bin/env python
# encoding: utf-8
"""
integer_to_roman.py

Created by Shengwei on 2014-07-27.
"""

# https://oj.leetcode.com/problems/integer-to-roman/
# tags: medium, numbers, roman, convert

"""
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""

# https://oj.leetcode.com/discuss/1208/how-to-improve-code

class Solution:
    mappings = (
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    )
    
    # @return a string
    def intToRoman(self, num):
        result = ''
        index = 0
        while num:
            base, roman = self.mappings[index]
            while num >= base:
                result += roman
                num -= base
            index += 1
        return result
