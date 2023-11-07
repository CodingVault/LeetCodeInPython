#!/usr/bin/env python
# encoding: utf-8
"""
palindrome_number.py

Created by Shengwei on 2014-07-10.
"""

# https://oj.leetcode.com/problems/palindrome-number/

"""
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
"""

# privous bug: use base instead of i in the loop (line "18")

class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        base, tmp = -1, x
        while tmp:
            base += 1
            tmp /= 10
        
        # x is 0 or single digit
        if base == -1 or base == 0:
            return True
        
        tmp = x
        for i in xrange(base, base / 2, -1):
            left, x = divmod(x, 10 ** i)
            tmp, right = divmod(tmp, 10)
            if left != right:
                return False
        
        return True
