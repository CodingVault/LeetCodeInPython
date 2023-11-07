#!/usr/bin/env python
# encoding: utf-8
"""
remove_dups_from_sorted_array.py

Created by Shengwei on 2014-07-06.
"""

# https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# tags: easy / medium, array, pointer, dups, logic

"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].
"""

# TODO: for cursor, check if A[cursor] != A[cursor-2] instead of A[cursor-1]
#   rewrite it following the pattern of remove_dups_from_sorted_array

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if A is None:
            return 0
        if len(A) <= 2:
            return len(A)
        
        stay, walker = 0, 1
        counter = 1
        while walker < len(A):
            if A[stay] == A[walker]:
                counter += 1
            else:
                counter = 1
            
            if counter <= 2:
                stay += 1
                if stay != walker:
                    A[stay] = A[walker]
            walker += 1
        
        return stay + 1
