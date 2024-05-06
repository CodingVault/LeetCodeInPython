#!/usr/bin/env python
# encoding: utf-8
"""
longest_consecutive_sequence.py

Created by Shengwei on 2014-07-13.
"""

# https://leetcode.com/problems/longest-consecutive-sequence/description/
# https://oj.leetcode.com/problems/longest-consecutive-sequence/
# tags: hard, array, numbers, hashtable, longest, tricky, union-find, disjoint set

"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""

class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        
        # store the mapping between low and high boundary
        cache = {}
        
        for i in nums:
            # note: do not process dups
            if i in cache: continue
            
            low = cache[i - 1] if i - 1 in cache else i
            high = cache[i + 1] if i + 1 in cache else i
            
            # IMPOTANT: server as a marker so it won't process dups
            cache[i] = i
            
            cache[low] = high
            cache[high] = low
        
        # note: numbers within a consecutive sequence
        #   won't point out of the boundary
        return max(abs(key - value) + 1
                   for key, value in cache.iteritems())
