#!/usr/bin/env python
# encoding: utf-8
"""
merge_intervals.py

Created by Shengwei on 2014-07-07.
"""

# https://oj.leetcode.com/problems/merge-intervals/
# tags: medium, array, interval

"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""

# ttps://gist.github.com/senvey/772e0afd345934cee475

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if intervals is None or len(intervals) <= 1:
            return intervals
        
        result = []
        intervals = sorted(intervals, key=lambda i: i.start)
        
        # this step must be after the intervals are sorted
        start, end = intervals[0].start, intervals[0].end
        
        for interval in intervals:
            n_start, n_end = interval.start, interval.end
            
            # becasue the intervals are sorted now, start
            # must be less than or equal to n_start, so
            # if n_start <= end, it starts in [start, end]
            if n_start <= end:
                if n_end >= end:
                    end = n_end
                # if n_end < end: pass
            else:
                result.append(Interval(start, end))
                start, end = n_start, n_end
        
        # IMPORTANT! remember to post-process
        result.append(Interval(start, end))
        return result
