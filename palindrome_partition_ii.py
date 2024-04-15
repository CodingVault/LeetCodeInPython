#!/usr/bin/env python
# encoding: utf-8
"""
palindrome_patition_ii.py

Created by Shengwei on 2014-07-29.
"""

# https://oj.leetcode.com/problems/palindrome-partitioning-ii/
# tags: hard, string, palindrome, dp, cached

"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""

# use built-in @cache: https://leetcode.com/problems/palindrome-partitioning-ii/solutions/1388628/python-simple-top-down-dp-clean-concise/

# 20240413 -- used sentinel
class Solution:
    def minCut(self, s: str) -> int:
        cuts = [-1]
        palindromes = set()
        
        for index in range(len(s)):
            min_cut = index
            for cursor in range(index + 1):
                if s[cursor] == s[index] and (index - cursor <= 2 or
                        (cursor + 1, index - 1) in palindromes):
                    palindromes.add((cursor, index))
                    min_cut = min(min_cut, cuts[cursor] + 1)
            
            cuts.append(min_cut)
        
        return cuts[-1]


# https://oj.leetcode.com/discuss/6691/my-dp-solution-explanation-and-code
# https://oj.leetcode.com/discuss/496/always-time-limit-exceeded

# TLE case: "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        cuts = []
        palindromes = set()
        
        # Lesson learned: function call can be very expensive;
        #   this function call increase running time for the case
        #   above from < 300ms to > 850ms.
        # def is_palindrome(i, j):
        #    if s[i] == s[j] and (
        #            j - i <= 2 or (i + 1, j - 1) in palindromes):
        #        palindromes.add((i, j))
        #        return True
        #    return False
        
        for index in range(len(s)):
            # s[:index + 1] requires at most `index` cuts
            min_cut = index
            for cursor in range(index + 1):
                # if the char at index can form palindrom with the sequence immediately prior to it,
                # the min_cut at index is (the min_cut prior to the palindrom) + 1
                if s[cursor] == s[index] and (index - cursor <= 2 or
                        (cursor + 1, index - 1) in palindromes):
                    palindromes.add((cursor, index))
                    # note: can add a sentiel to the beginning of `cuts` as `-1`,
                    #   or set cuts[0] = 0 and offset index by 1
                    if cursor == 0:
                        # do not shortcut and continue here;
                        # substring will not be checked for
                        # palindrome otherwise
                        min_cut = 0
                    else:
                        cut = cuts[cursor - 1] + 1
                        min_cut = min(min_cut, cut)
            
            cuts.append(min_cut)
        
        return cuts[-1]
