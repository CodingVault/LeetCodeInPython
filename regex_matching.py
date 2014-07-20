#!/usr/bin/env python
# encoding: utf-8
"""
regex_matching.py

Created by  on 2014-07-09.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/regular-expression-matching/

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