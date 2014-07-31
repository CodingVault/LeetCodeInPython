#!/usr/bin/env python
# encoding: utf-8
"""
wildcard_matching.py

Created by  on 2014-07-09; implemented on 2014-07-30.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/wildcard-matching/
# tags: medium / hard, string, matching, recursion, cached, optimization, logic

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
https://oj.leetcode.com/discuss/2964/still-get-tle-on-aaaaaaaaaaaaa-exhausted
1. if s[i] match p[j] or p[j] == '?', move forward;
2. if p[j] is '*', then keep j, and start a loop for i' until s[i'] == p[j+1];
3. restart from step 1

KEY POINT:
    a) if during the matching, there is another p[k] == '*' where k > j, and
        s[i'...i''] and p[j+1...k-1] match, we don't need to go back and check if prior
        '*' at p[j] may match more chars (it matches s[i...i'-1] in this case). This
        is because if p[k:] cannot match with s[i'':], p and s cannot match anyway.
    b) if p and s match, there must be a section in s exactly matches with the section
        between p[j] and p[k].

Alternatively:
    starting from the end of p going forward up to the first '*', if the section
    doesn't match the tail of s, they cannot match anyway. i.e., checking from the
    end backward can save comparing directly.
"""

# TODO: try alternative above (scan from the end) and plain scan from beginning

# https://oj.leetcode.com/discuss/1670/wildcard-match-tle-only-happens-on-java

############# AC version #############
# for the longest case: 100 loops, best of 3: 7.56 ms per loop
class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        s_length = len(s)
        p_length = len(p)
        
        def match(s_i, p_i):
            """0: match, 1: plain string not match, 2: terminate"""
            if p_length == p_i:
                return 0 if s_length == s_i else 1
            
            index = 0
            if s_length > s_i:
                while s_i + index < s_length and p_i + index < p_length:
                    if s[s_i + index] != p[p_i + index] and p[p_i + index] != '?':
                        # s and p don't match at current index
                        break
                    index += 1
            # s_i + index == len(s) and/or p_i + index == len(p) - or -
            # s[s_i + index] != p[p_i + index] if they exist
            
            if p_i + index < p_length and p[p_i + index] == '*':
                # p[p_i + index] == '*' matches 0 or 1 char in s
                result = match(s_i + index, p_i + index + 1)
                
                # note: if '*' matches 1 char in s, len(s[s_i:]) must be > 1
                if result == 1 and s_length > s_i:
                    result = match(s_i + index + 1, p_i + index)
                
                # terminate if no match for p[p_i:] starting with "*";
                #   it cannot match any part in s anyway
                return 0 if result == 0 else 2
            
            # p_i + index == len(p) or p[p_i + index] != ('*' or s[s_i + index]);
            # only if index == len(s[s_i:]) == len(p[p_i:]), p and s match
            if s_i + index == s_length:
                if p_i + index == p_length:
                    return 0
                
                if p_i + index < p_length:
                    # terminate if p[p_i:] is longer and does not start with "*";
                    # alternative: check this before recursion removes "*" at the
                    #   beginning of p[p_i:] in outer recrusion
                    return 2
            
            # somewhere in the middle of both string do not match, let outer
            # recursion continue to try wildcard matching if any
            return 1
        
        return True if match(0, 0) == 0 else False


############# cached with indices only #############
class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        cache = {}
        
        def match(s_i, p_i):
            if p_i == len(p):
                return True if s_i == len(s) else False
                
            if (s_i, p_i) in cache:
                return cache[(s_i, p_i)]
            
            index = 0
            if s[s_i:] != '':
                while s_i + index < len(s) and p_i + index < len(p):
                    if s[s_i + index] != p[p_i + index] and p[p_i + index] != '?':
                        # s and p don't match at current index
                        break
                    index += 1
            # index == len(s) and/or index == len(p) - or -
            # s[index] != p[index] if index < len(s) and index < len(p)
            
            if p_i + index < len(p) and p[p_i + index] == '*':
                # p[index] == '*' matches 0 or 1 char in s
                # note: if '*' matches 1 char in s, len(s) must be > 1
                result = (match(s_i + index, p_i + index + 1) or
                    len(s) > s_i and match(s_i + index + 1, p_i + index))
                cache[(s_i, p_i)] = result
                return result
            
            # index == len(p) or p[index] != ('*' or s[index]);
            # only if index == len(s) == len(p), p and s match
            if s_i + index == len(s) and p_i + index == len(p):
                cache[(s_i, p_i)] = True
            else:
                cache[(s_i, p_i)] = False
            return cache[(s_i, p_i)]
        
        return match(0, 0)


############# no cache #############
class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        if p == '':
            return True if s == '' else False
        
        index = 0
        if s != '':
            while index < len(s) and index < len(p):
                if s[index] != p[index] and p[index] != '?':
                    # s and p don't match at current index
                    break
                index += 1
        # index == len(s) and/or index == len(p) - or -
        # s[index] != p[index] if index < len(s) and index < len(p)
        
        if index < len(p) and p[index] == '*':
            # p[index] == '*' matches 0 or 1 char in s
            # note: if '*' matches 1 char in s, len(s) must be > 1
            return (self.isMatch(s[index:], p[index + 1:]) or
                len(s) > 1 and self.isMatch(s[index + 1:], p[index:]))
        
        # index == len(p) or p[index] != ('*' or s[index]);
        # only if index == len(s) == len(p), p and s match
        return True if index == len(s) and index == len(p) else False
