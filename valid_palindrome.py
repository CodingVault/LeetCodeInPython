#!/usr/bin/env python
# encoding: utf-8
"""
valid_palindrome.py

Created by Shengwei on 2014-07-02; updated on 2014-07-28.
"""

# https://oj.leetcode.com/problems/valid-palindrome/
# tags: easy, string

"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome
"""

############ V2 ############
class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if s == '':
            return True
        
        left, right = 0, -1
        while left - right < len(s):
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        
        return True

############ V1 ############
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
