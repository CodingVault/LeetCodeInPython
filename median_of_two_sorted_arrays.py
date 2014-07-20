#!/usr/bin/env python
# encoding: utf-8
"""
median_of_two_sorted_arrays.py

Created by  on 2014-07-15.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/median-of-two-sorted-arrays/

"""
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
"""

# except the last iteration (which discards the entire A),
# find_kth eliminates at least K/2 items per iteration,
# either in array A (A[pa] < B[pb]) or in array B (A[pa] > B[pb]).

def find_kth(A, base_a, B, base_b, k):
    """
    base_a, base_b: where to start checking (initially as 0)
    k: how many elements to select

    It is necessary and cannot be simply (len(A)+len(B))/2,
    because it's true the first time but not really the case
    in later iterations.
    """
    
    if len(A) - base_a > len(B) - base_b:
        return find_kth(B, base_b, A, base_a, k)

    if base_a == len(A):
        return float(B[base_b + k - 1])
    
    if k == 1:
        # the above two checks asserts A[base_a] and b[base_b]
        # are available
        return float(min(A[base_a], B[base_b]))

    # count how many elements to select in each array;
    # if k is odd, select one more element in B
    count_a = min(k / 2, len(A) - base_a)
    count_b = k - count_a
    
    index_a = base_a + count_a - 1
    index_b = base_b + count_b - 1
    
    if A[index_a] > B[index_b]:
        return find_kth(A, base_a, B, index_b + 1, k - count_b)
    if A[index_a] < B[index_b]:
        return find_kth(A, index_a + 1, B, base_b, k - count_a)
    return float(A[index_a])
        

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        total = len(A) + len(B)
        if total == 0:
            return 0.0
        
        if total % 2 == 0:
            return (
                find_kth(A, 0, B, 0, total / 2) +
                find_kth(A, 0, B, 0, total / 2 + 1)
            ) / 2.0
        return find_kth(A, 0, B, 0, total / 2 + 1)