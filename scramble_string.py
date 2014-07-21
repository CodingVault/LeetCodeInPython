#!/usr/bin/env python
# encoding: utf-8
"""
scramble_string.py

Created by  on 2014-07-20.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
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
