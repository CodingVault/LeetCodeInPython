#!/usr/bin/env python
# encoding: utf-8
"""
letter_combinations_of_phone_num.py

Created by  on 2014-07-20.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/letter-combinations-of-a-phone-number/
# tags: medium, numbers, string, recursion, generator, dfs

"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

[pic - mapping = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']]

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

mapping = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        
        def combine(s, remainder):
            if len(remainder) == 0:
                yield s
                return
            
            # note: str <--> int conversion
            for char in mapping[int(remainder[0])]:
                for x in combine(s + char, buffer(remainder, 1)):
                    yield x
        
        return list(combine('', digits))