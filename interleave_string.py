#!/usr/bin/env python
# encoding: utf-8
"""
interleave_string.py

Created by Shengwei on 2014-07-04.
"""

# https://oj.leetcode.com/problems/interleaving-string/
# tags: hard, string, stack, dp

"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
"""

# TODO: try to use memorized DP

class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s3) != len(s1) + len(s2):
            return False
        if s1 == s3 or s2 == s3:
            return True
        
        i1 = i2 = i3 = 0
        
        # store the states where it's okay to either increase
        # s2 or s3 -- s3[i3] == s1[i1] == s2[i2]
        stack = []
        
        # cache failed states
        #
        # states are added when it appears the first time;
        # the second time it appears, it must be because of
        # another state prior to current one; but both
        # possibility (increasing s1 or s2) for current state
        # must have been tried before trying prior states,
        # which means both possibility were failed, so we
        # don't need to add current state to the stack again
        cache = set()

        while i3 < len(s3):
            if (i1 < len(s1) and s3[i3] == s1[i1] and
                    i2 < len(s2) and s3[i3] == s2[i2]):
                state = (i1, i2, i3)
                if state not in cache:
                    stack.append(state)
                    cache.add(state)
            
            if i1 < len(s1) and s3[i3] == s1[i1]:
                # it could be only s1[i1] == s3[i3], while
                # it could be also s3[i3] == s1[i1] == s2[i2];
                # trying to increase i1 first anyway
                i1 += 1
            elif i2 < len(s2) and s3[i3] == s2[i2]:
                # s3[i3] == s2[i2] != s1[i1]
                i2 += 1
            elif stack:
                # s3[i3] != s1[i1] and s3[i3] != s2[i2], try
                # to restore previous state where
                # s3[i3] == s1[i1] == s2[i2], if any
                i1, i2, i3 = stack.pop()
                # increasing i1 has been tried, now trying i2
                i2 += 1
            else:
                return False
            
            i3 += 1
        
        return True
