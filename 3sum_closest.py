#!/usr/bin/env python
# encoding: utf-8
"""
3sum_closest.py

Created by  on 2014-07-25.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/3sum-closest/
# tags: medium, numbers, sum, search, edge cases

"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

"""

class Solution:
    # @return an integer
    def threeSumClosest(self, nums, target):
        
        nums = sorted(nums)
        one = nums[0] + 1
        closest = nums[0] + nums[1] + nums[2]
        for cursor in xrange(len(nums) - 2):
            if nums[cursor] == one:
                continue
            one = nums[cursor]
            
            i, j = cursor + 1, len(nums) - 1
            while i < j:
                three_sum = one + nums[i] + nums[j]
                if three_sum == target:
                    return target
                
                if abs(target - three_sum) < abs(target - closest):
                    closest = three_sum
                
                if three_sum > target:
                    j -= 1
                else:
                    i += 1
        
        return closest


class Solution:
    # @return an integer
    def threeSumClosest(self, nums, target):
        
        closest_dis = 10000000
        nums = sorted(nums)
        one = nums[0] + 1
        for cursor in xrange(len(nums) - 2):
            if nums[cursor] == one:
                continue
            one = nums[cursor]
            
            i, j = cursor + 1, len(nums) - 1
            while i < j:
                three_sum = one + nums[i] + nums[j]
                if three_sum == target:
                    return target
                
                if abs(target - three_sum) < abs(closest_dis):
                    closest_dis = three_sum - target
                
                if three_sum > target:
                    j -= 1
                else:
                    i += 1
        
        return closest_dis + target
