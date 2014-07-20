#!/usr/bin/env python
# encoding: utf-8
"""
first_missing_positive.py

Created by  on 2014-07-10.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/first-missing-positive/

"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""

# https://oj.leetcode.com/discuss/242/why-most-people-solve-this-problem-under-the-assumption-a-i-n
# https://oj.leetcode.com/discuss/4220/a-very-nice-solution-from-ants-aasma-%40stackoverflow

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        if A is None or len(A) == 0:
            return 1
        
        # first pass -- put `num` at index `num - 1` as index starts from 0
        for i in xrange(len(A)):
            num = A[i]
            while num > 0 and num <= len(A) and num != A[num - 1]:
                A[num - 1], num = num, A[num - 1]
        
        # scan through the array and find the first missing `num` at `num - 1`
        for i in xrange(1, len(A) + 1):
            if A[i - 1] != i:
                return i
        return len(A) + 1