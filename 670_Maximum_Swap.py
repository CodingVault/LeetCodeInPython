#!/usr/bin/env python
# encoding: utf-8
"""
670. Maximum Swap

Created by Shengwei on 2024-05-07.

Used:
- TikTok: https://www.1point3acres.com/bbs/thread-1065235-1-1.html
"""

# https://leetcode.com/problems/maximum-swap/description/
# tags: medium / hard, numbers, tricky, logic

"""
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

 

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
 

Constraints:

0 <= num <= 108
"""

# others:
# - https://leetcode.com/problems/maximum-swap/solutions/185982/straightforward-o-n-python/
#	- this is essentially the same as the "alternative solution", while there is no need
#		to actually do the swap as it is for bubble-sort
#	- the trick is when to update with max_id -- only when a smaller one for swap is found


# alternative solution utilizing one run of bubble-sort, O(n)
class Solution:
    def maximumSwap(self, num: int) -> int:
        chars = bytearray(str(num), 'utf-8')
        for i in range(-1, -len(chars), -1):
            if chars[i] > chars[i - 1]:
                chars[i], chars[i - 1] = chars[i - 1], chars[i]
        # print(''.join(chr(n) for n in chars))
        
        for i in range(len(chars)):
            if chr(chars[i]) != str(num)[i]:
                break
        largest, j = chars[i], i
        # print(largest, j)

        chars = bytearray(str(num), 'utf-8')
        for i in range(-1, -len(chars), -1):
            if largest == chars[i]:
                break
        
        chars[i], chars[j] = chars[j], chars[i]
        return int(chars.decode())


# this solution is a bit tricky, encoutering lots of edge cases to evolve
# - the oi must be held (as `hold_i`) for repetition and used to swap later
# - `hold_i` has to be reset to 0 correctly (i.e., after repetition)
# - edge cases: 98368, 1993, 91993
# this solution also requires sorting so it's O(nlogn)
class Solution:
    def maximumSwap(self, num: int) -> int:
        chars = bytearray(str(num), 'utf-8')
        # note: 
        # - `reversed` returns an iterator, while `sorted` returns a list
        # - `sorted` also takes `reverse` arg
        cache = sorted(((n, i) for i, n in enumerate(chars)), reverse=True)
        # print(cache)
        
        for i in range(len(cache)):
            n, oi = cache[i]

            if i == 0 or cache[i - 1][0] != n:
                hold_i = 0

            if i + 1 < len(cache) and cache[i + 1][0] == n and hold_i < oi:
                hold_i = oi
                
            swap_i = hold_i or oi
            if i < swap_i and chars[i] < chars[swap_i]:
                chars[i], chars[swap_i] = chars[swap_i], chars[i]
                break
        return int(chars.decode())