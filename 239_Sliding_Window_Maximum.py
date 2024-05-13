#!/usr/bin/env python
# encoding: utf-8
"""
239. Sliding Window Maximum

Created by Shengwei on 2025-05-08, submitted on 2018-09-22.

Used:
- TikTok: https://www.1point3acres.com/bbs/thread-1064522-1-1.html
"""

# https://leetcode.com/problems/sliding-window-maximum/description/
# tags: hard, array, window, tricky, starred

"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums: return []
        
        from collections import deque
        
        res = []
        holder = deque()  # hold indices of possible max values
        for i in range(len(nums)):
            # remove from tail whichever numbers at the index are
            # smaller than the one at current index i
            while holder and nums[holder[-1]] < nums[i]:
                holder.pop()
            holder.append(i)
            
            # remove head of the stack if the index is out of window
            start = i - k + 1
            if holder[0] < start:
                holder.popleft()
            
            # start to add numbers to result until the first window fills
            if start >= 0:
                res.append(nums[holder[0]])
                
        return res
