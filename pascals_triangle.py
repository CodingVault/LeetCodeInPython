#!/usr/bin/env python
# encoding: utf-8
"""
pascals_triangle.py

Created by  on 2014-07-03.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/pascals-triangle/

"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows <= 0:
            return []
        
        res = [[1]]
        if numRows == 1:
            return res
        
        for _ in xrange(1, numRows):
            cur_level = []
            upper_level = res[-1]
            left = right = 0
            
            for j in xrange(len(upper_level)):
                left = right  # for j == 0, left would be 0
                right = upper_level[j]
                cur_level.append(left + right)
            
            # append the right most 1
            cur_level.append(1)
            res.append(cur_level)
        
        return res