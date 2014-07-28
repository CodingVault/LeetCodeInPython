#!/usr/bin/env python
# encoding: utf-8
"""
gray_code.py

Created by  on 2014-07-15.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/gray-code/
# tags: medium / hard, numbers, logic, recursion

"""
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.
"""

class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n == 0:
            return [0]
    
        sub_code = self.grayCode(n - 1)
        reversed_code = []
        for code in reversed(sub_code):
            reversed_code.append(code | 1 << n - 1)
    
        return sub_code + reversed_code