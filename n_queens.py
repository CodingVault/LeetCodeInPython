#!/usr/bin/env python
# encoding: utf-8
"""
n_queens.py

Created by Shengwei on 2014-07-23.
"""

# https://oj.leetcode.com/problems/n-queens/
# tags: medim / hard, matrix, bit manipulation, generator, dfs, edge cases, bitmap, tricky

"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""

# https://oj.leetcode.com/discuss/3861/solved-with-backtracing
# https://oj.leetcode.com/discuss/743/whats-your-solution

class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        
        positions = (1 << n) - 1
        
        def search(board, depth, vertical_taken, left_taken, right_taken):
            if depth == 0:
                yield board
                return
            
            line = ['.'] * n
            # it must be & with positions, otherwise it's a negative number
            # with all 1's extending to the leftmost bit
            availables = positions & ~(vertical_taken | left_taken | right_taken)
            
            # loop through all the availables at this depth
            while availables:
                pos = availables & (-availables)  # get the rightmost bit that is 1
                availables -= pos  # remove current pos from availables
                index = int(math.log(pos, 2))  # compute the index where to put queen
                
                # note: remember the recursive call is an iterater and yield again
                line[index] = 'Q'
                for each in search(
                        board + [''.join(line)], depth - 1, vertical_taken + pos,
                        left_taken + pos << 1, right_taken + pos >> 1):
                    yield each
                line[index] = '.'
        
        return list(search([], n, 0, 0, 0))
