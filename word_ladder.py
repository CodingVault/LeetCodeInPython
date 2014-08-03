#!/usr/bin/env python
# encoding: utf-8
"""
word_ladder.py

Created by Shengwei on 2014-07-02.
"""

# https://oj.leetcode.com/problems/word-ladder/
# tags: medium, string, bfs, word

"""
Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
"""

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dictionary, a set of string
    # @return an integer
    def ladderLength(self, start, end, dictionary):
        """
        Performance note:
         - use set instead of list for `visited`
         - the order in `new_word in dict and new_word not in visited` is important:
            for long distance between `start` and `end`, `visited` can become huge
            while `dict` is of constant size.
        """
        if start == end:
            return 1
        
        all_chars = map(chr, xrange(ord('a'), ord('z') + 1))
        visited = set()
        bfs = [start, None]
        
        # at which distance the following to-be-processed nodes are
        distance = 2
        
        while len(bfs) > 1:
            word = bfs.pop(0)
            if word is None:
                distance += 1
                bfs.append(None)
                continue
            
            for i in xrange(len(word)):
                for char in all_chars:
                    new_word = word[:i] + char + word[i + 1:]
                    if new_word == end:
                        return distance
                    if new_word in dictionary and new_word not in visited:
                        bfs.append(new_word)
                        visited.add(new_word)
        
        return 0
