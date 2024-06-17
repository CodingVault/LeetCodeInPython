#!/usr/bin/env python
# encoding: utf-8
"""
227. Basic Calculator II

Created by Shengwei on 2024-06-17.

Used:
- Snap: https://www.1point3acres.com/bbs/thread-1064167-1-1.html
"""

# https://leetcode.com/problems/basic-calculator-ii/description/
# tags: medium / hard, stack, logic

"""
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "3+2*2"
Output: 7


Example 2:

Input: s = " 3/2 "
Output: 1


Example 3:

Input: s = " 3+5 / 2 "
Output: 5
 

Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
"""

# https://leetcode.com/problems/basic-calculator-ii/solutions/63076/python-short-solution-with-stack/
# https://leetcode.com/problems/basic-calculator-ii/solutions/63004/17-lines-c-easy-20-ms/ <-- non-stack version


# non-stack version
class Solution:
    def calculate(self, s: str) -> int:
        res = last = cur = 0
        sign = '+'

        for i in range(len(s) + 1):
            if i < len(s):
                c = s[i]
                if c.isdigit():
                    cur = cur * 10 + int(c)
                    continue
                if c == ' ':
                    continue
            
            # print(res, last, sign, cur)
            if sign in ('+', '-'):
                res += last
                last = cur if sign == '+' else -cur
            else:
                # more complicated in Python as -5 // 2 = -3
                if cur > 0:  # has to check cur here, otherwise throw divided by zero error (should never happen)
                    tmp = last // cur if last > 0 or last % cur == 0 else last // cur + 1
                else:
                    tmp = 0
                last = last * cur if sign == '*' else tmp
            
            sign = c
            cur = 0
        
        return res + last


# alternative: use flag to circumvent negative integer divide issue in Python
class Solution:
    def calculate(self, s: str) -> int:
        res = last = cur = 0
        sign = '+'
        negative = False

        for i in range(len(s) + 1):
            if i < len(s):
                c = s[i]
                if c.isdigit():
                    cur = cur * 10 + int(c)
                    continue
                if c == ' ':
                    continue
            
            # print(res, last, '-' if negative else '+', sign, cur)
            if sign in ('+', '-'):
                res += last if not negative else -last
                # note: update the flag only after it's used and current sign in ('+', '-')
                negative = sign == '-'
                last = cur
            else:
                last = last * cur if sign == '*' else last // cur
            
            sign = c
            cur = 0
        
        # note: don't forget to use `negative` here as well
        return res + last if not negative else res - last
