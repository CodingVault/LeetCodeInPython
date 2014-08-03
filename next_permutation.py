#!/usr/bin/env python
# encoding: utf-8
"""
next_permutation.py

Created by Shengwei on 2014-07-08; implemented on 2014-08-01.
"""

# https://oj.leetcode.com/problems/next-permutation/
# tags: medium, numbers, permutation, logic

"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

# 1. search from right to left and stop at first number num(i) that is less than num(i+1)
# 2. switch num(i) with the least greater number in num[i:0]
# 3. reverse all the numbers in num[i:-1]

class Solution:
    # @param nums, a list of integer
    # @return a list of integer
    def nextPermutation(self, nums):
        
        for index in xrange(-1, -len(nums) - 1, -1):
            if nums[index] < nums[-1]:
                for switch in xrange(index + 1, 0):
                    if nums[switch] > nums[index]:
                        nums[switch], nums[index] = nums[index], nums[switch]
                        return nums
            
            # move nums[index] to the end of the list
            tmp = nums[index]
            for cursor in xrange(index, -1):
                nums[cursor] = nums[cursor + 1]
            nums[-1] = tmp
        
        # the list was descending, return the ascending one
        return nums
