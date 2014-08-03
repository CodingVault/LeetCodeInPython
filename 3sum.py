#!/usr/bin/env python
# encoding: utf-8
"""
3sum.py

Created by Shengwei on 2014-07-24.
"""

# https://oj.leetcode.com/problems/3sum/
# tags: medium / hard, numbers, sum, search, dups, edge cases, optimization

"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
"""

# https://oj.leetcode.com/discuss/2319/getting-tle-with-o-n-2-solution
# AC: 1000 loops, best of 3: 362 µs per loop

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        
        nums = sorted(nums)
        length = len(nums)
        result = []
        one = nums[0] + 1  # sentinel
        for cursor in xrange(length - 2):
            if nums[cursor] == one:
                continue
            one = nums[cursor]
            
            i, j = cursor + 1, length - 1
            while i < j:
                # note: don't use sentinel here since the num can be
                #   the same as last loop, but should not be the same
                #   as prior num in the array
                if i > cursor + 1 and nums[i] == nums[i - 1]:
                    i += 1
                    continue
                
                two = nums[i]
                three = nums[j]
                three_sum = one + two + three
                if three_sum == 0:
                    result.append([one, two, three])
                    i += 1
                    j -= 1
                elif three_sum < 0:
                    i += 1
                else:
                    j -= 1
        
        return result


################ even faster ################
# 1000 loops, best of 3: 456 µs per loop

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        
        nums = sorted(nums)
        length = len(nums)
        result = []
        for cursor in xrange(1, length - 1):
            if cursor < length - 2 and nums[cursor] == nums[cursor + 1]:
                continue
            
            sub_sums = collections.defaultdict(set)
            two = nums[cursor]
            one = nums[0] + 1  # sentinel
            for index in xrange(cursor):
                if nums[index] == one:
                    continue
                
                one = nums[index]
                sub_sums[one + two].add((one, two))
            
            three = -nums[cursor + 1] + 1  # sentinel
            for index in xrange(cursor + 1, length):
                if nums[index] == three:
                    continue
                
                three = nums[index]
                if -three in sub_sums:
                    for pair in sub_sums[-three]:
                        result.append([pair[0], pair[1], three])
        
        return result


################ hashtable + binary search ################
# 1000 loops, best of 3: 762 µs per loop

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        
        nums = sorted(nums)
        result = []
        two = nums[1] + 1  # sentinel
        for cursor in xrange(1, len(nums) - 1):
            if nums[cursor] == two:
                continue
            
            sub_sums = collections.defaultdict(set)
            two = nums[cursor]
            one = nums[0] + 1  # sentinel
            for index in xrange(cursor):
                if nums[index] == one:
                    continue
                
                one = nums[index]
                sub_sums[one + two].add((one, two))
            
            # binary search for -sub_sum if any
            for sub_sum, pairs in sub_sums.iteritems():
                left, right = index + 1, len(nums)
                while left < right:
                    mid = (left + right) / 2
                    if nums[mid] == -sub_sum:
                        for pair in pairs:
                            result.append([pair[0], pair[1], -sub_sum])
                        break
                    if nums[mid] > -sub_sum:
                        right = mid
                    else:
                        left = mid + 1
        
        return result


################ simple but slow ################

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, nums):

        def generator():
            for index in xrange(len(nums) - 2):
                one = nums[index]
                for i in xrange(index + 1, len(nums) - 1):
                    two = nums[i]
                    for j in xrange(i + 1, len(nums)):
                        if one + two + nums[j] == 0:
                            yield tuple(sorted((one, two, nums[j])))

        return map(list, set(generator()))
