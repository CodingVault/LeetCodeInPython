#!/usr/bin/env python
# encoding: utf-8
"""
215. Kth Largest Element in an Array

Created by Shengwei on 2023-10-08.

Used:
* Meta: https://www.1point3acres.com/bbs/thread-1026967-1-1.html
"""

# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
# tags: easy / medium, array, sorting, heap

"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?


Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""

# quick select: https://leetcode.com/problems/kth-largest-element-in-an-array/solutions/1019513/python-quickselect-average-o-n-explained/


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heap = nums[:k]
        heapq.heapify(heap)

        for i in range(k, len(nums)):
            heapq.heappushpop(heap, nums[i])
        
        return heap[0] if heap else -1
