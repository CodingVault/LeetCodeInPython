#!/usr/bin/env python
# encoding: utf-8
"""
search_for_range.py

Created by Shengwei on 2014-07-13.
"""

# https://oj.leetcode.com/problems/search-for-a-range/
# tags: medium, array, search

"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""

# https://oj.leetcode.com/discuss/529/the-elements-the-whole-array-the-same-the-target-can-logn-time
# alternative:
#   1. search for the target in the original array
#   2. search for the target in the left half until it cannot find the target -- left boundary
#   3. search for the target in the right half until it cannot find the target -- right boundary

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        if A is None or len(A) == 0:
            return [-1, -1]
        
        start = end = -1
        
        left, right = 0, len(A)
        while left < right:
            mid = (left + right) / 2
            if A[mid] >= target:
                if A[mid] == target:
                    start = mid
                right = mid
            else:
                left = mid + 1
        
        left, right = 0, len(A)
        while left < right:
            mid = (left + right) / 2
            if A[mid] <= target:
                if A[mid] == target:
                    end = mid
                left = mid + 1
            else:
                right = mid
        
        return [start, end]


class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        if A is None or len(A) == 0:
            return [-1, -1]

        def bin_search(n):
            left, right = 0, len(A)
            while left < right:
                mid = (left + right) / 2
                if A[mid] == n:
                    return mid
                if A[mid] > n:
                    right = mid
                else:
                    left = mid + 1
            return right

        # note:
        #   1. index can be len(A) if target doesn't exist in A
        #   2. don't search for `target-1`, for example, in case of dups
        index = bin_search(target)
        if index < len(A) and A[index] == target:
            return [bin_search(target - 0.5), bin_search(target + 0.5) - 1]
        else:
            return [-1, -1]
