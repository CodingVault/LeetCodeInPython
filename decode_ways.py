#!/usr/bin/env python
# encoding: utf-8
"""
decode_ways.py

Created by  on 2014-07-29.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/decode-ways/
# tags: medium, numbers, string, dp, recursion

"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""

############## iterative version ##############
class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if s == '':
            return 0
        
        cache, index = [], 0
        while index < len(s):
            ways = 0
            
            single = int(s[index])
            if single > 0 and single < 10:
                # alternative: single in range(1, 10)
                ways += cache[index - 1] if index > 0 else 1
            
            if index > 0:
                double = int(s[index - 1:index + 1])
                if double > 9 and double < 27:
                    # alternative: double in range(10, 28)
                    ways += cache[index - 2] if index > 1 else 1
            
            cache.append(ways)
            index += 1
        
        return cache[-1]

############## recursive version ##############
class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if s == '':
            return 0
        
        ways = 0
        if int(s[0]) > 0 and int(s[0]) < 27:
            if s[1:] == '': return 1
            ways += self.numDecodings(s[1:])
        if int(s[:2]) > 9 and int(s[:2]) < 27:
            if s[:2] == '': return ways + 1
            ways += self.numDecodings(s[2:])
        return ways
