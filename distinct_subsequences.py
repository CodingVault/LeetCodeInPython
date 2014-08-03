#!/usr/bin/env python
# encoding: utf-8
"""
distinct_subsequence.py

Created by Shengwei on 2014-07-28.
"""

# https://oj.leetcode.com/problems/distinct-subsequences/
# tags: hard, string, dp

"""
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
"""

############ iterative version ############
class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        m, n = len(T), len(S)
        # T as rows and S as cols
        matrix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            # len(S) == 0, len(T) > 0
            matrix[i][0] = 0
        for j in range(n + 1):
            # len(S) > 0, len(T) == 0
            matrix[0][j] = 1
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                x = matrix[i][j - 1]
                y = matrix[i - 1][j - 1]
                y = y if T[i - 1] == S[j - 1] else 0
                matrix[i][j] = x + y
        
        return matrix[-1][-1]

############ recursive version ############
class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        if len(S) < len(T):
            return 0
        if T == '':
            return 1
        
        x = self.numDistinct(S[:-1], T)
        y = self.numDistinct(S[:-1], T[:-1])
        y = y if S[-1] == T[-1] else 0
        
        return x + y
