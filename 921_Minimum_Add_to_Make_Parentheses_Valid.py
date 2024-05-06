#!/usr/bin/env python
# encoding: utf-8
"""
921. Minimum Add to Make Parentheses Valid

Created by Shengwei on 2023-11-06.

Used:
* Meta: https://www.1point3acres.com/bbs/thread-1026007-1-1.html
"""

# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/
# tags: easy, parentheses, logic

"""
A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.

 

Example 1:

Input: s = "())"
Output: 1


Example 2:

Input: s = "((("
Output: 3


Constraints:

1 <= s.length <= 1000
s[i] is either '(' or ')'.
"""

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        lc = rc = 0
        for c in s:
            if c == '(':
                lc += 1
            elif c == ')':
                if lc:
                    lc -= 1
                else:
                    rc += 1
        return lc + rc
