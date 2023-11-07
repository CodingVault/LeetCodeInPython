#!/usr/bin/env python
# encoding: utf-8
"""
multiply_strings.py

Created by Shengwei on 2014-07-28.
"""

# https://oj.leetcode.com/problems/multiply-strings/
# tags: medium, string, D&C

"""
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
"""

class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        if int(num1) == 0 or int(num2) == 0:
            return '0'
        
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        
        # multiply digit by digit (remember to convert char to int)
        to_sum = []
        base = 0
        for i in reversed(num1):
            multiply = [0] * base
            carry = 0
            for j in reversed(num2):
                carry, remainder = divmod(int(i) * int(j) + carry, 10)
                multiply.append(remainder)
            if carry:
                multiply.append(carry)
            to_sum.append(multiply)
            base += 1
        
        # sum up all the sub sums via D&C
        def sumup(start, end):
            if start + 1 == end:
                return to_sum[start]
            
            mid = (start + end) / 2
            x = sumup(start, mid)
            y = sumup(mid, end)
            
            z = []
            index = carry = 0
            while index < len(x) or index < len(y):
                i = x[index] if index < len(x) else 0
                j = y[index] if index < len(y) else 0
                carry, remainder = divmod(i + j + carry, 10)
                z.append(remainder)
                index += 1
            if carry:
                z.append(carry)
            
            return z
        
        # remember to reverse the list
        return ''.join(map(str, reversed(sumup(0, len(to_sum)))))
