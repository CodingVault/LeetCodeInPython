#!/usr/bin/env python
# encoding: utf-8
"""
4sum.py

Created by Shengwei on 2014-07-21; AC on 2014-07-31.
"""

# https://oj.leetcode.com/problems/4sum/
# tags: hard, numbers, sum, hashtable, search, dups, logic, optimization

"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
"""


############ AC version ############
# https://oj.leetcode.com/discuss/3950/tle-on-4sum-using-hashtable
# 10 loops, best of 3: 27.2 ms per loop

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, nums, target):
        nums = sorted(nums)
        result = set()
        # cache all the seen sub-sum of any two numbers prior to current cursor
        cache  = collections.defaultdict(set)
        
        for i in range(len(nums)):  # more strictly -- for i in range(1, len(nums) - 1)
            # find supplimentray sub-sum in cache for the sub-sum of current cursor and any number after it
            for j in range(i + 1, len(nums)):
                for half in cache[target - nums[i] - nums[j]]:
                    result.add(tuple(list(half) + [nums[i], nums[j]]))
            
            # cache the sub-sum of current cursor and any number prior to it
            for k in range(i):
                cache[nums[i] + nums[k]].add((nums[k], nums[i]))
        
        return map(list, result)


############ without two sum but using `set` (faster) ############
# 10 loops, best of 3: 158 ms per loop. TLE on test case: [91277418,66271374,38763793,4092006,11415077,60468277,1122637,72398035,-62267800,22082642,60359529,-16540633,92671879,-64462734,-55855043,-40899846,88007957,-57387813,-49552230,-96789394,18318594,-3246760,-44346548,-21370279,42493875,25185969,83216261,-70078020,-53687927,-76072023,-65863359,-61708176,-29175835,85675811,-80575807,-92211746,44755622,-23368379,23619674,-749263,-40707953,-68966953,72694581,-52328726,-78618474,40958224,-2921736,-55902268,-74278762,63342010,29076029,58781716,56045007,-67966567,-79405127,-45778231,-47167435,1586413,-58822903,-51277270,87348634,-86955956,-47418266,74884315,-36952674,-29067969,-98812826,-44893101,-22516153,-34522513,34091871,-79583480,47562301,6154068,87601405,-48859327,-2183204,17736781,31189878,-23814871,-35880166,39204002,93248899,-42067196,-49473145,-75235452,-61923200,64824322,-88505198,20903451,-80926102,56089387,-58094433,37743524,-71480010,-14975982,19473982,47085913,-90793462,-33520678,70775566,-76347995,-16091435,94700640,17183454,85735982,90399615,-86251609,-68167910,-95327478,90586275,-99524469,16999817,27815883,-88279865,53092631,75125438,44270568,-23129316,-846252,-59608044,90938699,80923976,3534451,6218186,41256179,-9165388,-11897463,92423776,-38991231,-6082654,92275443,74040861,77457712,-80549965,-42515693,69918944,-95198414,15677446,-52451179,-50111167,-23732840,39520751,-90474508,-27860023,65164540,26582346,-20183515,99018741,-2826130,-28461563,-24759460,-83828963,-1739800,71207113,26434787,52931083,-33111208,38314304,-29429107,-5567826,-5149750,9582750,85289753,75490866,-93202942,-85974081,7365682,-42953023,21825824,68329208,-87994788,3460985,18744871,-49724457,-12982362,-47800372,39958829,-95981751,-71017359,-18397211,27941418,-34699076,74174334,96928957,44328607,49293516,-39034828,5945763,-47046163,10986423,63478877,30677010,-21202664,-86235407,3164123,8956697,-9003909,-18929014,-73824245], -236727523

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, nums, target):
        nums = sorted(nums)
        
        result = set()
        for b in xrange(1, len(nums) - 2):
            # stores sub_sums for the new num index just moved on
            sub_sums = {}
            
            for a in xrange(b):
                sub_sums[nums[a] + nums[b]] = [nums[a], nums[b]]
            
            for c in xrange(b + 1, len(nums) - 1):
                for d in xrange(c + 1, len(nums)):
                    remainder = target - nums[c] - nums[d]
                    if remainder in sub_sums:
                        result.add(tuple(
                           sub_sums[remainder]  + [nums[c], nums[d]]))
        
        return map(list, result)

# slight variation below but it's slower

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, nums, target):
        nums = sorted(nums)
        
        result = set()
        sub_sums = collections.defaultdict(list)
        for index in xrange(1, len(nums) - 2):
            for i in xrange(index):
                sub_sums[nums[i] + nums[index]].append([nums[i], nums[index]])
            
            for cursor in xrange(index + 1, len(nums) - 1):
                for i in xrange(cursor + 1, len(nums)):
                    remainder = target - nums[cursor] - nums[i]
                    for half in sub_sums[remainder]:
                        result.add(tuple(half  + [nums[cursor], nums[i]]))
        
        return map(list, result)

# optimized two sum version with about same running time
# 10 loops, best of 3: 190 ms per loop

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, nums, target):
        nums = sorted(nums)
        result = []
        
        for a in xrange(len(nums) - 3):
            if a > 0 and nums[a] == nums[a - 1]: continue
        
            for b in xrange(a + 1, len(nums) - 2):
                if b > a + 1 and nums[b] == nums[b - 1]: continue
                
                # two sum for the other half
                half = nums[a] + nums[b]
                c, d = b + 1, len(nums) - 1
                while c < d:
                    total = half + nums[c] + nums[d]
                    if total == target:
                        result.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1
                        # inner loop is almost twice faster than if..continue
                        # for checking each num in nums[b + 1...len(nums) - 1]
                        while c < d and nums[c] == nums[c - 1]:
                            c += 1
                        while c < d and nums[d] == nums[d + 1]:
                            d -= 1
                    elif total < target:
                        c += 1
                    else:
                        d -= 1
        
        return result


############ faster two sum O(n^3) ############
# using `set` instead of control dups manually
# 1 loops, best of 3: 189 ms per loop

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, nums, target):
        nums = sorted(nums)
        
        def two_sum(start, target):
            end = len(nums) - 1
            result = set()
            while start < end:
                sub_sum = nums[start] + nums[end]
                if sub_sum == target:
                    result.add((nums[start], nums[end]))
                    start += 1
                    end -= 1
                elif sub_sum > target:
                    end -= 1
                else:
                    start += 1
            return result
        
        result = set()
        for index in xrange(1, len(nums) - 2):
            # stores sub_sums for the new num index just moved on
            sub_sums = {}
            
            for i in xrange(index):
                sub_sum = nums[i] + nums[index]
                sub_sums[sub_sum] = [nums[i], nums[index]]
            
            for sub_sum, half in sub_sums.iteritems():
                for sub_set in two_sum(index + 1, target - sub_sum):
                    result.add(tuple(half + list(sub_set)))
        
        return map(list, result)


############ two sum O(n^3) ############

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, nums, target):
        nums = sorted(nums)
        
        def two_sum(start, target):
            left, right = start, len(nums) - 1
            while left < right:
                if left > start and nums[left] == nums[left-1]:
                    left += 1
                    continue
                if right < len(nums) - 1 and nums[right] == nums[right+1]:
                    right -= 1
                    continue
                
                sub_sum = nums[left] + nums[right]
                if sub_sum == target:
                    yield [nums[left], nums[right]]
                    left += 1
                    right -= 1
                elif sub_sum > target:
                    right -= 1
                else:
                    left += 1
        
        def generator():
            for index in xrange(1, len(nums) - 2):
                # there is a bug here, for test case ([0, 0, 0, 0], 0)
                if nums[index] == nums[index - 1]:
                    continue
                
                # stores sub_sums for the new num index just moved on
                sub_sums = {}
                
                for i in xrange(index):
                    sub_sum = nums[i] + nums[index]
                    sub_sums[sub_sum] = [nums[i], nums[index]]
                
                for sub_sum, half in sub_sums.iteritems():
                    for sub_set in two_sum(index + 1, target - sub_sum):
                        yield half + sub_set
        
        return list(generator())


############ (nearly) brute force O(n^3) ############

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, nums, target):
        nums = sorted(nums)
        
        def generator():
            for index in xrange(1, len(nums) - 2):
                # incorrect: it skips the possibility of combination with
                #   nums[index - 1], nums[index] and two other bigger numbers
                if nums[index] == nums[index - 1]:
                    continue
                
                # stores sub_sums for the new num index just moved on
                sub_sums = {}
                
                for i in xrange(index):
                    sub_sum = nums[i] + nums[index]
                    sub_sums[sub_sum] = [nums[i], nums[index]]
                
                for cursor in xrange(index + 1, len(nums) - 1):
                    # note: skip only when (cursor > index + 1)
                    #   think the case [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8
                    if cursor > index + 1 and nums[cursor] == nums[cursor - 1]:
                        continue
                    for i in xrange(cursor + 1, len(nums)):
                        # note: similar situation as above
                        if i > cursor + 1 and nums[i] == nums[i - 1]:
                            continue
                        remainder = target - nums[cursor] - nums[i]
                        if remainder in sub_sums:
                            yield sub_sums[remainder] + [nums[cursor], nums[i]]
        
        return list(generator())

############ plain three loops O(n^3) ############
# 1 loops, best of 3: 506 ms per loop

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, nums, target):
        nums = sorted(nums)
        result = []

        for a in xrange(len(nums) - 3):
            if a > 0 and nums[a] == nums[a - 1]: continue

            for b in xrange(a + 1, len(nums) - 2):
                if b > a + 1 and nums[b] == nums[b - 1]: continue

                rest = set(nums[b + 1:])
                for c in xrange(b + 1, len(nums) - 1):
                    if c > b + 1 and nums[c] == nums[c - 1]: continue
                    rest.remove(nums[c])
                    d = target - nums[a] - nums[b] - nums[c]
                    if d in rest:
                        result.append([nums[a], nums[b], nums[c], d])

        return result
