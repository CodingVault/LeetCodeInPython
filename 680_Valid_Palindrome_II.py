#!/usr/bin/env python
# encoding: utf-8
"""
680. Valid Palindrome II

Created by Shengwei on 2022-04-18.
"""

# https://leetcode.com/problems/valid-palindrome-ii/
# tags: easy / medium, string, palindrome

"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true

Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s: return True
        
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                break
            left += 1
            right -= 1
        
        passed = True
        l, r = left + 1, right
        while l < r:
            if s[l] != s[r]:
                passed = False
                break
            l += 1
            r -= 1
        
        if passed: return True
        l, r = left, right - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True


class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s: return True
        
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                break
            left += 1
            right -= 1
        
        def is_pal(s):
            return s == s[::-1]
        
        return is_pal(s[left+1:right+1]) or is_pal(s[left:right])
