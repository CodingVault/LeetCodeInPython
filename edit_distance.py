#!/usr/bin/env python
# encoding: utf-8
"""
edit_distance.py

Created by  on 2014-07-28.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/edit-distance/
# tags: medium, string, dp

"""
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
"""

# alternative: get the max common subsequence `mcs`,
#   edit distance = max(len(s1, s2)) - len(mcs)

############ iterative version ############
class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        len1, len2 = len(word1), len(word2)
        # word1 as rows and word2 as cols
        matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        for i in range(len1 + 1):
            matrix[i][0] = i
        for j in range(len2 + 1):
            matrix[0][j] = j
        
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                x = matrix[i - 1][j] + 1
                y = matrix[i][j - 1] + 1
                z = matrix[i - 1][j - 1]
                # note: word index = matrix index - 1
                z += 0 if word1[i - 1] == word2[j - 1] else 1
                matrix[i][j] = min(x, y, z)
        
        return matrix[-1][-1]

############ recursive version ############
class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        if word1 == '' or word2 == '':
            return max(len(s1), len(s2))
        
        x = self.minDistance(word1[:-1], word2) + 1
        y = self.minDistance(word1, word2[:-1]) + 1
        z = self.minDistance(word1[:-1], word2[:-1])
        z += 0 if word1[-1] == word2[-1] else 1
        
        return min(x, y, z)
