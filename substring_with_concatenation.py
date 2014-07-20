#!/usr/bin/env python
# encoding: utf-8
"""
substring_with_concatenation.py

Created by  on 2014-07-08.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/substring-with-concatenation-of-all-words/

"""
You are given a string, S, and a list of words, L, that are all of the same length. Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

For example, given:
S: "barfoothefoobarman"
L: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
"""

# 1. there could be dups in L
# 2. substring can start at any index, even within previously matched substring
# 3. optimization: set marker prior to the loop instead of building marker in the loop

class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        if L is None or len(L) == 0:
            return []
        word_length = len(L[0])
            
        if S is None or len(S) < word_length:
            return []
        
        # in case there are dups in L
        marker = dict((s, L.count(s)) for s in set(L))
        
        result = []
        # early termination
        for i in xrange(len(S) - word_length * len(L) + 1):
            
            sub_s = S[i:i+word_length]
            if sub_s in L:
                counter = 0
                cursor = i
                marker_copy = marker.copy()
                
                while counter < len(L) and sub_s in L:
                    marker_copy[sub_s] -= 1
                    if marker_copy[sub_s] < 0:
                        break
                    
                    counter += 1
                    cursor += word_length
                    sub_s = S[cursor:cursor+word_length]
                
                if counter == len(L):
                    result.append(i)
        
        return result