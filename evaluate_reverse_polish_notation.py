#!/usr/bin/env python
# encoding: utf-8
"""
evaluate_reverse_polish_notation.py

Created by  on 2014-06-30.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/evaluate-reverse-polish-notation/

"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        
        stack = []
        for token in tokens:
            if token.isdigit() or token[1:].isdigit():
                stack.append(int(token))
                continue
    
            right_op = stack.pop()
            left_op = stack.pop()
            if token == '+':
                stack.append(left_op + right_op)
            elif token == '-':
                stack.append(left_op - right_op)
            elif token == '*':
                stack.append(left_op * right_op)
            elif token == '/':
                stack.append(int(float(left_op) / right_op))
        
        return stack.pop()