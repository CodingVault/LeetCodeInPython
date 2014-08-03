#!/usr/bin/env python
# encoding: utf-8
"""
sudoku_solver.py

Created by  on 2014-08-02.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/sudoku-solver/
# tags: medium / hard, matrix, sudoku, optimization, bit manipulation, dfs, bitmap

"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
"""

# https://oj.leetcode.com/discuss/5958/afraid-cant-solve-problem-interview-because-someone-simplify

# timeit board = map(list, [".....7..9",".4..812..","...9...1.","..53...72","293....5.",".....53..","8...23...","7...5..4.","531.7...."]); Solution().solveSudoku(board)

############ bitmap ############
# 10 loops, best of 3: 27 ms per loop
class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        positions = (1 << 9) - 1
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty_cells = []
        
        # mark all the existing numbers
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty_cells.append((i, j))
                    continue
                # pos = pow(2, num - 1)
                pos = 1 << (int(board[i][j]) - 1)
                box = i / 3 * 3 + j / 3
                rows[i] |= pos
                cols[j] |= pos
                boxes[box] |= pos
        
        def solve(empty_cell_index):
            if empty_cell_index >= len(empty_cells):
                return True
            row, col = empty_cells[empty_cell_index]
            box = row / 3 * 3 + col / 3
            availables = positions & ~(rows[row] | cols[col] | boxes[box])
            while availables:
                pos = availables & -availables
                availables ^= pos  # remove pos from availables
                rows[row] |= pos
                cols[col] |= pos
                boxes[box] |= pos
                if solve(empty_cell_index + 1):
                    num = str(int(math.log(pos, 2)) + 1)
                    board[row][col] = num
                    return True
                rows[row] ^= pos
                cols[col] ^= pos
                boxes[box] ^= pos
            return False
        
        solve(0)

############ brute force ############
# 1 loops, best of 3: 392 ms per loop
class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        
        def is_valid(row, col):
            char = board[row][col]
            for j in range(9):
                if j != col and board[row][j] == char:
                    return False
            for i in range(9):
                if i != row and board[i][col] == char:
                    return False
            box_i, box_j = row / 3 * 3, col / 3 * 3
            for i in range(box_i, box_i + 3):
                for j in range(box_j, box_j + 3):
                    if i != row and j != col and board[i][j] == char:
                        return False
            return True
        
        def solve(row, col):
            if col == 8:
                next_row = row + 1
                next_col = 0
            else:
                next_row = row
                next_col = col + 1
            
            if board[row][col] != '.' and (row < 8 or col < 8):
                return solve(next_row, next_col)
            
            for num in range(1, 10):
                board[row][col] = str(num)
                if is_valid(row, col):
                    if row == 8 and col == 8:
                        return True
                    elif solve(next_row, next_col):
                        return True
            board[row][col] = '.'
            return False
        
        solve(0, 0)
