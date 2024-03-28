#!/usr/bin/env python
# encoding: utf-8
"""
zigzag_conversion.py

Created by Shengwei on 2014-07-15.
"""

# https://oj.leetcode.com/problems/zigzag-conversion/
# tags: medium, string, logic, edge cases

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""

class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:
            return s

        # index difference between two virtical columns
        virtical_interval = (nRows - 1) * 2
        
        res = ''
        for row in xrange(nRows):
            index = row
            while index < len(s):
                res += s[index]
                distance = nRows - 1 - row
                if row > 0 and distance > 0:
                    next_index = index + 2 * distance
                    if next_index < len(s):
                        res += s[next_index]

                index += virtical_interval
        
        return res
