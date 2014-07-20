#!/usr/bin/env python
# encoding: utf-8
"""
word_ladder.py

Created by  on 2014-07-02.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/word-ladder/

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
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
                    if new_word in dict and new_word not in visited:
                        bfs.append(new_word)
                        visited.add(new_word)
    
        return 0