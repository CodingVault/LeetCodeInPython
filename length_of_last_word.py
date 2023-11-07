#!/usr/bin/env python
# encoding: utf-8
"""
length_of_last_word.py

Created by Shengwei on 2014-07-23.
"""

# https://oj.leetcode.com/problems/length-of-last-word/
# tags: easy / medium, string, pointer, edge cases, invariant
# edge cases: "a ", " a", " ", "         "

"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.
"""

# https://oj.leetcode.com/discuss/4749/need-a-more-optimized-code
# TODO: try different approaches -- move starting from the end

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        
        if s == '' or s == ' ':
            return 0
        
        # ensure that start points only on non-space char;
        # also if start is -1 in the end, there is no word
        start = 0 if s[0] != ' ' else -1
        end = start
        scanner = 1
        
        while scanner < len(s):
            if s[scanner] == ' ':
                # note: do not combine two `if` statements
                #   or do not use `elif` below
                if s[scanner - 1] != ' ':
                    # found the end of current word
                    end = scanner
            
            elif s[scanner - 1] == ' ':
                # move watcher when scanner points a char
                # following an empty space (new word)
                start = scanner
            
            scanner += 1
        
        if s[-1] == ' ':
            return end - start
        return len(s) - start


#####################################
# consider the problem "abc " to be answered with 0, treating the last word as and empty one

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        if len(s) == 0:
            return 0
        
        watcher = scanner = 0
        restart = False
        while scanner < len(s):
            if s[scanner] == ' ':
                # move watcher for next non-space char
                restart = True
            
            elif restart:
                # move watcher when scanner doesn't point
                # at a space and it's not on the same word
                watcher = scanner
                restart = False
            
            scanner += 1
        
        # there are empty spaces in the end
        return 0 if restart else scanner - watcher
