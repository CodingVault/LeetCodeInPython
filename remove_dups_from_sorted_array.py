#!/usr/bin/env python
# encoding: utf-8
"""
remove_dups_from_sorted_array.py

Created by Shengwei on 2014-07-23.
"""

# https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array/
# tags: easy, array, pointer, dups, logic, optimization

"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].
"""

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) <= 1:
            return len(A)
        
        writer = finder = 1
        while finder < len(A):
            if A[finder] != A[finder - 1]:
                # note: be careful where to put this; writer needs
                #   to increase when finder doesn't point at a dup
                # minor optimization: don't write to its own pos
                if finder > writer:
                    A[writer] = A[finder]
                writer += 1
            finder += 1
        
        return writer
