#!/usr/bin/env python
# encoding: utf-8
"""
wildcard_matching.py

Created by  on 2014-07-09.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/wildcard-matching/

"""
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
"""

"""
1. if s[i] match p[j] or p[j] == '?', move forward;
2. if p[j] is '*', move to p[j+1], and start a loop for i until s[i] == p[j];
3. restart from step 1
"""