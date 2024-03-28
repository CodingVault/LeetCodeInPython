#!/usr/bin/env python
# encoding: utf-8
"""
410. Split Array Largest Sum

Created by Shengwei on 2023-10-28.
"""

# https://leetcode.com/problems/split-array-largest-sum/description/
# tags: hard, array, number, binary

"""
Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.

 

Example 1:

Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
Example 2:

Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.
 

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 106
1 <= k <= min(50, nums.length)
"""

# greedy: go from left to right and sum up to a limit --> results in the least number of splits

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        start, end = max(nums), sum(nums)
        while start < end:
            mid = (start + end) // 2

            # note: count should start with 1 instead of 0,
            #   or +1 after the loop to count for the last split
            count, total = 1, 0
            for num in nums:
                total += num
                if total > mid:
                    count += 1
                    total = num
            
            # note: should not return just yet
            # if count == k:
            #     return mid

            if count > k:
                start = mid + 1
            else:
                end = mid
        
        # note: "end" is either sum(nums) or some value that
        #   has been validated as "mid"
        return end
