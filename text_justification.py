#!/usr/bin/env python
# encoding: utf-8
"""
text_justification.py

Created by Shengwei on 2014-08-03.
"""

# https://oj.leetcode.com/problems/text-justification/
# tags: medium, string, array, edge cases

"""
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.

Corner Cases:
A line other than the last line might contain only one word. What should you do in this case?
In this case, that line should be left-justified.
"""

class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        result = []
        line, l = [words[0]], len(words[0])
        for word in words[1:]:
            if l + 1 + len(word) <= L:
                # the next word can still fit on current line
                l += 1
            
            elif len(line) == 1:
                # note: special case -- only one word
                result.append(line.pop().ljust(L))
                l = 0
                
            else:
                # current line is full, process it
                extra, remainder = divmod(L - l, len(line) - 1)
                s = line[0]
                extra += 1
                for w in line[1:]:
                    blank = ' ' * extra
                    if remainder:
                        blank += ' '
                        remainder -= 1
                    s += blank + w
                result.append(s)
                # note: remember to reset for the next line
                line, l = [], 0
            
            # suppose len(word) <= L
            line.append(word)
            l += len(word)
        
        # note: remember to process the last line
        result.append(' '.join(line).ljust(L))
        
        return result
