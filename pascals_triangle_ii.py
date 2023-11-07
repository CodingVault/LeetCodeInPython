#!/usr/bin/env python
# encoding: utf-8
"""
pascals_triangle_ii.py

Created by Shengwei on 2014-07-03.
"""

# https://oj.leetcode.com/problems/pascals-triangle-ii/
# tags: easy / medium, triangle, dp

"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""

############ dp ############
# TODO

############ V1 ############
class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        """Computes the next level in place."""
        if rowIndex < 0:
            return []
        
        res = [1]
        if rowIndex == 0:
            return res

        for _ in xrange(rowIndex):
            res.insert(0, 1)
            # note: len(res) has increased by 1
            
            for j in xrange(1, len(res) - 1):
                res[j] = res[j] + res[j + 1]
        
        return res
