#!/usr/bin/env python
# encoding: utf-8
"""
count_and_say.py

Created by Shengwei on 2014-07-27.
"""

# https://oj.leetcode.com/problems/count-and-say/
# tags: medium / hard, numbers

"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""

class Solution:
    # @return a string
    def countAndSay(self, n):
        num = '1'
        
        for _ in xrange(n - 1):
            c, count = num[0], 1
            tmp = ''
            for index in xrange(1, len(num)):
                if num[index] == num[index - 1]:
                    count += 1
                else:
                    tmp += str(count) + c
                    c, count = num[index], 1
            num = tmp + str(count) + c
            
        return num
