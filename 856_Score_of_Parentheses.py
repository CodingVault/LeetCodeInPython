#!/usr/bin/env python
# encoding: utf-8
"""
856. Score of Parentheses

Created by Shengwei on 2025-05-10.

Used:
- TikTok: https://www.1point3acres.com/bbs/thread-1061850-1-1.html
"""

# https://leetcode.com/problems/score-of-parentheses/description/
# tags: medium / hard, logic, parantheses, recursion, stack

"""
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:

Input: s = "()"
Output: 1

Example 2:

Input: s = "(())"
Output: 2

Example 3:

Input: s = "()()"
Output: 2
 

Constraints:

2 <= s.length <= 50
s consists of only '(' and ')'.
s is a balanced parentheses string.
"""

# v3
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                else:
                    score = 0
                    while stack[-1] != '(':
                        score += 2 * stack.pop()
                    stack.pop()
                    stack.append(score)
        
        return sum(stack)


# v2
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        def process(pos):
            score = 0
            lc = 0
            while pos < len(s):
                if s[pos] == '(':
                    lc += 1
                    if s[pos+1] == ')':  # '()'
                        score += 1
                    else:  # '(('
                        t_score, pos = process(pos + 1)
                        score = 2 * t_score
                else:
                    lc -= 1  # '))'
                    if pos + 1 < len(s) and s[pos+1] == '(':  # ')('
                        t_score, pos = process(pos + 1)
                        score += t_score
                
                if not lc:
                    return score, pos
                pos += 1
            
        return process(0)[0]


# v1
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        lc = 0
        start = 0
        for i in range(len(s)):
            if s[i] == '(':
                lc += 1
            else:
                lc -= 1

            i += 1
            if lc == 0:
                sub_s = s[start:i]
                if sub_s == '()':
                    score += 1
                else:
                    score += 2 * self.scoreOfParentheses(sub_s[1:-1])
                start = i
        return score
