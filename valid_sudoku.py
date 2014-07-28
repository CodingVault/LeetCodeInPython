#!/usr/bin/env python
# encoding: utf-8
"""
valid_sudoku.py

Created by  on 2014-07-27.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/valid-sudoku/
# tags: medium, matrix, sudoku, bit manipulation

"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules (http://sudoku.com.au/TheRules.aspx).

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
"""

# https://oj.leetcode.com/discuss/5655/valid-sudoku-tle

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                
                pos = 1 << int(board[i][j])
                box = i / 3 * 3 + j / 3
                if rows[i] & pos or cols[j] & pos or boxes[box] & pos:
                    return False
                rows[i] |= pos
                cols[j] |= pos
                boxes[box] |= pos
        
        return True
