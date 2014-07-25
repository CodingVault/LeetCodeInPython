#!/usr/bin/env python
# encoding: utf-8
"""
search_in_rotated_array.py

Created by  on 2014-07-15.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/search-in-rotated-sorted-array/
# tags: medium, array, search, rotated, edge cases

"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        if A is None or len(A) == 0:
            return -1
        
        left, right = 0, len(A)
        while left < right:
            mid = (left + right) / 2
            if A[mid] == target:
                return mid
            
            if target < A[mid]:
                if A[left] > A[mid] or A[left] <= target:
                    right = mid
                else:
                    left = mid + 1
            else:
                if A[right - 1] < A[mid] or A[right - 1] >= target:
                    left = mid + 1
                else:
                    right = mid
        
        return -1
