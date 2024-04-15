#!/usr/bin/env python
# encoding: utf-8
"""
gray_code.py

Created by Shengwei on 2014-07-15.
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


# TODO: iterative way


# 20240330
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]

        sub = self.grayCode(n - 1)

        # effectively add 0 to the right
        ext_0 = [x << 1 for x in sub]

        # effectively add 1 to the right
        ext_1 = [(x << 1) + 1 for x in sub]

        return ext_0 + list(reversed(ext_1))


class Solution:
    # @return a list of integers
    def grayCode(self, n):
        """ grayCode(2) -> [00, 01, 11, 10]
            grayCode(3):
                - add 0 to the left of gc(2) -> [000, 001, 011, 010]
                - add 1 to the left of reversed gc(2) -> [110, 111, 101, 100]
                - piece them together: [000, 001, 011, 010, 110, 111, 101, 100]
        """
        if n == 0:
            return [0]
    
        sub_code = self.grayCode(n - 1)
        # the following is the same as:
        #   reversed_code = [code | 1 << n - 1 for code in reversed(sub_code)]
        reversed_code = []
        for code in reversed(sub_code):
            # sign priority: -, <<, |
            # essentially: code | (1 << (n - 1))
            reversed_code.append(code | 1 << n - 1)
    
        return sub_code + reversed_code
