#!/usr/bin/env python
# encoding: utf-8
"""
1249. Minimum Remove to Make Valid Parentheses

Created by Shengwei on 2023-11-04.

Used:
* Meta: https://www.1point3acres.com/bbs/thread-1026092-1-1.html
"""

# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/
# tags: medium, string, logic

"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
 

Constraints:

1 <= s.length <= 105
s[i] is either'(' , ')', or lowercase English letter.
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        def process(array, left, right):
            cursor = lcnt = 0
            for b in array:
                if b == ord(left):
                    lcnt += 1
                if b == ord(right):
                    if lcnt:
                        lcnt -= 1
                    else:
                        continue
                array[cursor] = b
                cursor += 1
            array[cursor:] = []
        
        array = bytearray(s, 'utf-8')
        process(array, '(', ')')
        array = array[::-1]
        process(array, ')', '(')
        return array[::-1].decode('utf-8')



# others' better way:
#	1. record all the positions for '('
#	2. 1) if found matching ')', drop one position of '('
#	   2) if no '(' available, clear ')'
#	3. clear all '(' with positions still registered
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ""
        while stack:
            s[stack.pop()] = ""
        return "".join(s)
