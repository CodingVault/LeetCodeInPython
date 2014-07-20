#!/usr/bin/env python
# encoding: utf-8
"""
palindrome_partition.py

Created by  on 2014-07-02.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/palindrome-partitioning/
# tags: medium, string, dp, palindrome, dfs

"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]
"""

# time complexity:
#   to solve n chars, it needs to call is_palindrome several times.
#   f(n) = 1 + f(n-1) + 1 + f(n-2) + ... + 1 + f(1) + 1
#        = n + f(n-1) + f(n-2) + ... + f(1)
#        = n + n - 1 + f(n-2) + f(n-3) + ... + f(1)  # no 2f(n-2) due to cache
#        = O(n^2) times of calls to is_palindrome -- for O(n^2) substrings

# possibly better solution, pre-compute is_palindrome; maybe no gain
# https://oj.leetcode.com/discuss/5976/any-way-to-reduce-the-runtime

def is_palindrome(s):
    if len(s) < 2:
        return True

    left, right = 0, -1
    while left - right < len(s):
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

        
cache = {}

def recursive_par(s):
    if s in cache:
        return cache[s]
    
    if len(s) == 1:
        return [[s]]
    
    res = []
    for i in xrange(len(s)):
        sub, remainder = s[:i+1], s[i+1:]
        if is_palindrome(sub):
            if remainder == '':
                res.append([sub])
                continue
            
            pars = recursive_par(remainder)
            if pars:
                cache[remainder] = pars
            for par in pars:
                res.append([sub] + par)
    
    return res

class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        return recursive_par(s)
