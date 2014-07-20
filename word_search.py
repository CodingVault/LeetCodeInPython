#!/usr/bin/env python
# encoding: utf-8
"""
word_search.py

Created by  on 2014-07-05.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/word-search/

"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""

def get_marker(m, n):
    return [[0] * m for _ in xrange(n)]


def match(board, marker, row, col, word):
    if (row >= 0 and row < len(board) and
            col >= 0 and col < len(board[row])):

        if (not marker[row][col] and word[0] == board[row][col]):
            sub_word = word[1:]
            if not sub_word:
                return True

            marker[row][col] = 1
            if any([
                match(board, marker, row - 1, col, sub_word),
                match(board, marker, row + 1, col, sub_word),
                match(board, marker, row, col - 1, sub_word),
                match(board, marker, row, col + 1, sub_word)
            ]):
                return True
            else:
                marker[row][col] = 0

    return False


class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        if len(board) == 0:
            return False

        marker = get_marker(len(board[0]), len(board))
        return any(
            match(board, marker, row, col, word)
            for row in xrange(len(board))
            for col in xrange(len(board[row])))