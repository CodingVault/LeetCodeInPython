#!/usr/bin/env python
# encoding: utf-8
"""
search_in_rotated_array_ii.py

Created by  on 2014-07-24.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/search-in-rotated-sorted-array-ii/
# tags: medium / hard, array, search, rotated, edge cases

"""
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
"""

"""
General approach for searching in rotated sorted array:
1. determine which side is sorted by comparing A[left] with A[mid]
2. if target is in the sorted range, continue searching in that range;
    otherwise, searching in another half
"""

class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        left, right = 0, len(A)
        
        while left < right:
            mid = (left + right) / 2
            if A[mid] == target:
                return True
            
            if A[left] < A[mid]:
                # left half is sorted
                if A[left] <= target and target < A[mid]:
                    right = mid
                else:
                    left = mid + 1
            elif A[left] > A[mid]:
                # right half is sorted
                if A[mid] < target and target <= A[right-1]:
                    left = mid + 1
                else:
                    right = mid
            else:
                # cannot decide
                left += 1
        
        return False