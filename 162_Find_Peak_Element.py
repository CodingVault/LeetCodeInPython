#!/usr/bin/env python
# encoding: utf-8
"""
162. Find Peak Element

Created by Shengwei on 2023-10-08.

Used:
* Meta: https://www.1point3acres.com/bbs/thread-1026967-1-1.html
"""

# https://leetcode.com/problems/find-peak-element/description/
# tags: medium, array, binary search

"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 

Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.
"""

# O(log n)
# https://leetcode.com/problems/find-peak-element/solutions/1290642/intuition-behind-conditions-complete-explanation-diagram-binary-search/
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1

        left, right = 1, len(nums) - 2
        # note: need to double check the case when left == right
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1
        return -1

# linear
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = -sys.maxsize * 2
        nums.append(left)
        for i in range(len(nums) - 1):
            if nums[i] > left and nums[i] > nums[i + 1]:
                return i
            left = nums[i]
        # better - revert nums as it was: nums.pop()
        return -1
