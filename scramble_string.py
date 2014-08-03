#!/usr/bin/env python
# encoding: utf-8
"""
scramble_string.py

Created by Shengwei on 2014-07-20.
"""

# https://oj.leetcode.com/problems/scramble-string/
# tags: hard, string, dp, recursion

"""
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
"""

# https://oj.leetcode.com/discuss/3632/any-better-solution

"""
TODO: memorized version:
1. build the base case for strings of length 1
2. to compute if two strings of length m are scarmble strings, it needs to break them into two parts and
    there are O(m), i.e., O(n), ways to break one string; checking if two substrings are scramble strings
    can be done in constant time by utilizing the results of sub-problems; there are O(n-m), i.e., O(n),
    strings of length m; thus there are O(n^2) pairs of strings of length m to compare, and total O(n^3)
    time complexity for solving the problem if all pairs of substrings of length m are scramble strings
3. for substrings of length 1 to length n, the running time will be O(n^4)
"""

########## brute force ##########

class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        # print s1, s2
        if s1 == s2: return True
        if sorted(s1) != sorted(s2): return False
        
        for i in xrange(1, len(s1)):
            ls1, rs1 = s1[:i], s1[i:]
            ls2, rs2 = s2[:i], s2[i:]
            rls2, rrs2 = s2[:-i], s2[-i:]
            
            if (self.isScramble(ls1, ls2) and self.isScramble(rs1, rs2) or
                    self.isScramble(ls1, rrs2) and self.isScramble(rs1, rls2)):
                # print 'yes:', s1, s2
                return True
        
        return False
