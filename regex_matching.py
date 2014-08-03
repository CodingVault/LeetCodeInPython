#!/usr/bin/env python
# encoding: utf-8
"""
regex_matching.py

Created by Shengwei on 2014-07-09.
"""

# https://oj.leetcode.com/problems/regular-expression-matching/
# tags: medium / hard, string, matching, recursion

"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""

"""
1. if p[j+1] != '*', check (s[i] == p[j] or p[j] == '.') and match(s[i+1:], p[j+1:])
2. if p[j+1] == '*':
    1) if p[j] == '.', check:
        a) match(s[i], p[j+2]) -- '.*' matches 0 char on s, or
        b) match(s[i+1], p[j]) -- '.*' matches at least 1 char on s
    2) if p[j] != '.', check:
        a) match(s[i], p[j+2]) -- if s[i] != p[j], or
        b) match(s[i+1], p[j]) -- if s[i] == p[j]
2`. if p[j+1] == '*', check: (incorrect)
    1) match(s[i], p[j+2]) -- does not match any
    2) (s[i] == p[j] or p[j] == '.') and match(s[i+1], p[j]) (incorrect)
"""

############# cached #############

cache = {}

class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        if (s, p) in cache:
            return cache[(s, p)]
        
        if p == '': return s == ''
        
        if s == '':
            for i in xrange(0, len(p), 2):
                if i + 1 >= len(p) or p[i + 1] != '*':
                    cache[(s, p)] = False
                    return False
            cache[(s, p)] = True
            return True
        
        # len(s) > 0
        if len(p) == 1 or p[1] != '*':
            result = ((s[0] == p[0] or p[0] == '.') and
                self.isMatch(s[1:], p[1:]))
            cache[(s, p)] = result
            return result
        
        # len(p) > 1 and p[1] == '*'
        result = ((s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p)
                  or self.isMatch(s, p[2:]))
        cache[(s, p)] = result
        return result


############# TLE #############

class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        print s, p
        if p is None or s is None:
            return not (p or s)
        if p == '': return s == ''
        
        if s == '':
            for i in xrange(0, len(p), 2):
                if i + 1 >= len(p) or p[i + 1] != '*':
                    return False
            return True
        
        # len(s) > 0
        if len(p) == 1 or p[1] != '*':
            return ((s[0] == p[0] or p[0] == '.') and
                self.isMatch(s[1:], p[1:]))
        
        # len(p) > 1 and p[1] == '*'
        return ((p[0] == '.' or s[0] == p[0]) and self.isMatch(s[1:], p)
                or self.isMatch(s, p[2:]))
