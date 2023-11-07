#!/usr/bin/env python
# encoding: utf-8
"""
search_insert_position.py

Created by Shengwei on 2014-07-15.
"""

# https://oj.leetcode.com/problems/search-insert-position/
# tags: easy, array, search

"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        left, right = 0, len(A)
        while left < right:
            mid = (left + right) / 2
            if A[mid] == target:
                return mid
            if A[mid] > target:
                right = mid
            else:
                left = mid + 1
        
        # return right also works
        return left
