#!/usr/bin/env python
# encoding: utf-8
"""
valid_palindrome.py

Created by  on 2014-07-02.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/valid-palindrome/

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if s == '':
            return True
        
        left, right = 0, -1
    
        while True:
            
            while left < len(s) and not s[left].isalnum():
                left += 1
            while right >= -len(s) and not s[right].isalnum():
                right -= 1
    
            if left - right > len(s):
                return True
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1