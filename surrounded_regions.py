#!/usr/bin/env python
# encoding: utf-8
"""
surrounded_regions.py

Created by  on 2014-07-15.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/surrounded-regions/

"""
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
"""

# https://oj.leetcode.com/discuss/6454/dp-bfs-solution-o-n

def get_marker(m, n):
    return [[0] * m for _ in xrange(n)]

def flip(board, row, col, value):
    char_array = list(board[row])
    char_array[col] = value
    board[row] = ''.join(char_array)

def mark_escaped(board, row, col, marker):
    bsf = [(row, col)]
    while bsf:
        row, col = bsf.pop(0)
        if row >= 0 and row < len(board) and col >= 0 and col < len(board[row]):
            if board[row][col] == 'O' and marker[row][col] != -1:
                marker[row][col] = -1
                bsf.append((row, col - 1))
                bsf.append((row, col + 1))
                bsf.append((row - 1, col))
                bsf.append((row + 1, col))

class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if len(board) < 3 or len(board[0]) < 3:
            return
    
        marker = get_marker(len(board[0]), len(board))
    
        for i in xrange(0, len(board)):
            mark_escaped(board, i, 0, marker)
            mark_escaped(board, i, len(board[i]) - 1, marker)
        for j in xrange(0, len(board[0])):
            mark_escaped(board, 0, j, marker)
            mark_escaped(board, len(board) - 1, j, marker)
        
        for i in xrange(1, len(board) - 1):
            for j in xrange(1, len(board[i]) - 1):
                if marker[i][j] != -1 and board[i][j] == 'O':
                    flip(board, i, j, 'X')
