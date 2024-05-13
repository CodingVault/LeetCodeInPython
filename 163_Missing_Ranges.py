#!/usr/bin/env python
# encoding: utf-8
"""
163. Missing Ranges

Created by Shengwei on 2023-10-28.

Used:
- TikTok (20240510): https://www.1point3acres.com/bbs/thread-1063465-1-1.html
"""

# Locked
# tags: easy, array, number

"""
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
"""

def missing_range(array, low, high):
    res = []
    s = e = low

    for n in array:
        while e < n:
            e += 1
        if s == e - 1:
            res.append('{}'.format(s))
        elif s < e:
            res.append('{}->{}'.format(s, e - 1))
        s = e = n + 1

    if s == high:
        res.append('{}'.format(s))
    elif s < high:
        res.append('{}->{}'.format(s, high))

    return res
