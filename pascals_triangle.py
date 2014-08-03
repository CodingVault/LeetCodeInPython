#!/usr/bin/env python
# encoding: utf-8
"""
pascals_triangle.py

Created by Shengwei on 2014-07-03.
"""

# https://oj.leetcode.com/problems/pascals-triangle/
# tags: easy / medium, triangle, dp

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

############ dp ############
def triangle(n):
    if n == 1:
        return [[1]]
    
    sub_tria = triangle(n - 1)
    last_line, new_line = sub_tria[-1], []
    for i in range(len(last_line)):
        if i == 0:
            new_line.append(1)
            continue
        new_line.append(last_line[i] + last_line[i - 1])
    new_line.append(1)
    
    return sub_tria + [new_line]

############ V1 ############
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
