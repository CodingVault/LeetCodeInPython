#!/usr/bin/env python
# encoding: utf-8
"""
anagrams.py

Created by Shengwei on 2014-07-21.
"""

# https://oj.leetcode.com/problems/anagrams/
# tags: medium, string, hashtable

"""
Given an array of strings, return all groups of strings that are anagrams.

Note: All inputs will be in lower-cas
"""

def get_marker(s):
    # note: do not sort s; sorting stats is consistent time 
    #   since len(stats) is at most 26
    stats = dict((c, s.count(c)) for c in s)
    return ''.join('%s%s' % (key, stats[key]) for key in sorted(stats))

class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        # note: do not use `set` when strs can have dups
        mappings = collections.defaultdict(list)
        for s in strs:
            mappings[get_marker(s)].append(s)
        
        result = []
        for anagrams in mappings.values():
            if len(anagrams) > 1:
                result.extend(anagrams)
        
        return list(result)
