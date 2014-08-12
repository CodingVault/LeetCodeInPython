#!/usr/bin/env python
# encoding: utf-8
"""
longest_palindrome_substring.py

Created by Shengwei on 2014-07-16; updated on 2014-07-31.
"""

# https://oj.leetcode.com/problems/longest-palindromic-substring/
# tags: hard, string, palindrome, optimization

"""
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
"""

############# O(n) #############
# TODO


# http://www.mitbbs.com/article/JobHunting/32755595_0.html
class Solution:
    def longestPalindrome(self, s):
        longest, mid = "", (len(s) - 1) / 2
        i, j = mid, mid
        while i >= 0 and j < len(s):
            args = [(s, i, i), (s, i, i + 1), (s, j, j), (s, j, j + 1)]
            for arg in args:
                tmp = self.longestPalindromeByAxis(*arg)
                if len(tmp) > len(longest):
                    longest = tmp
            if len(longest) >= i * 2:
                return longest
            i, j = i - 1, j + 1
        return longest
        
    def longestPalindromeByAxis(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left, right = left - 1, right + 1
        return s[left + 1 : right]


############# O(n^2) #############
# http://blog.shengwei.li/leetcode-longest-palindromic-substring/
class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if s is None or len(s) == 0:
            return ''

        half = len(s) / 2

        def max_palindrome(left, right, min_length):
            """Gets the longest palindrom in s[left:right+1] centered at
            index (left + right) / 2"""
            if right - left < min_length:
                return ''
            start = left
            while left < right:
                if s[left] != s[right]:
                    if right - left < min_length:
                        return ''
                    start = left + 1
                left += 1
                right -= 1

            length = (left - start) * 2 + (right - left + 1)
            return s[start:start+length]

        def is_palindrome(left, right):
            """Checks if s[left:right+1] is a palindrome."""
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def get_max(left, cur_s, right, max_palin):
            """Gets maximum extensible boundary as a palindrome
            centered with cur_s."""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                cur_s = s[left] + cur_s + s[right]
                left -= 1
                right += 1

            return cur_s if len(cur_s) > len(max_palin) else max_palin
        
        def process_short(max_palin):
            for distance in xrange(half + 1):
                for sign in (-1, 1):
                    i = half + sign * distance
                    # even palindrome
                    max_palin = get_max(i - 1, '', i, max_palin)
                    # odd palindrome
                    if i < len(s):
                        max_palin = get_max(i - 1, s[i], i + 1, max_palin)
                
                max_half = min(i, len(s) - i)
                if len(max_palin) == max_half * 2:
                    return max_palin
            
            return max_palin
        
        if len(s) <= 500:
            return process_short(s[0])

        if is_palindrome(0, len(s) - 1):
            return s
        max_palin = ''
        for i in range(1, half):
            if is_palindrome(i, len(s) - 1) and len(s[i:len(s)]) > len(max_palin):
                max_palin = s[i:len(s)]
        for j in range(half, len(s) - 1):
            if is_palindrome(0, j) and len(s[:j + 1]) > len(max_palin):
                max_palin = s[:j + 1]

        if not max_palin:
            cur_max = self.longestPalindrome(s[:half])
            if len(cur_max) > len(max_palin):
                max_palin = cur_max
            cur_max = self.longestPalindrome(s[half:])
            if len(cur_max) > len(max_palin):
                max_palin = cur_max

        if len(max_palin) >= half:
            return max_palin
        
        return process_short(max_palin)

############# Optimized #############
class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if s is None or len(s) == 0:
            return ''
            
        def max_palindrome(left, right, min_length):
            if right - left < min_length:
                return ''
            start = left
            while left < right:
                if s[left] != s[right]:
                    if right - left < min_length:
                        return ''
                    start = left + 1
                left += 1
                right -= 1
            
            length = (left - start) * 2 + (right - left + 1)
            return s[start:start+length]
        
        max_palin = s[0]
        for distance in xrange(len(s) / 2):
            # distance needs to be (len(s) / 2) to reach index 0 but we don't
            # need to process index 0 as it's the center of palindrome itself
            for sign in (-1, 1):
                i = len(s) / 2 + sign * distance
                
                # odd palindrome
                max_half = min(i, len(s) - i - 1)
                cur_max = max_palindrome(i - max_half, i + max_half, len(max_palin))
                if len(cur_max) > len(max_palin):
                    max_palin = cur_max
                
                # even palindrome
                max_half = min(i, len(s) - i)
                cur_max = max_palindrome(i - max_half, i + max_half - 1, len(max_palin))
                if len(cur_max) > len(max_palin):
                    max_palin = cur_max
        
        return max_palin

############# naive solution #############
class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if s is None or len(s) == 0:
            return ''

        def get_max(left, cur_s, right, max_palin):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                cur_s = s[left] + cur_s + s[right]
                left -= 1
                right += 1

            return cur_s if len(cur_s) > len(max_palin) else max_palin
        
        max_palin = s[0]
        for i in xrange(1, len(s)):
            # even palindrome
            max_palin = get_max(i - 1, '', i, max_palin)
            # odd palindrome
            max_palin = get_max(i - 1, s[i], i + 1, max_palin)
        
        return max_palin

