#!/usr/bin/env python
# encoding: utf-8
"""
n_queens_ii.py

Created by Shengwei on 2014-07-31.
"""

# https://oj.leetcode.com/problems/n-queens-ii/
# tags: medium / hard, matrix, bit manipulation, generator, dfs, bitmap

"""
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
"""

# Note: pay attention to operation priority

class Solution:
    # @return an integer
    def totalNQueens(self, n):
        positions = (1 << n) - 1
        def solve(vertical, left, right, n):
            if n == 0:
                yield 1
                return
            
            availables = positions & ~(vertical | left | right)
            while availables:
                # get the rightmost available pos
                pos = availables & -availables
                
                # remove pos from availables
                availables ^= pos
                
                # take up corresponding pos on markers for the next row
                yield sum(solve(vertical | pos, (left | pos) << 1, (right | pos) >> 1, n - 1))
        
        return sum(solve(0, 0, 0, n))
