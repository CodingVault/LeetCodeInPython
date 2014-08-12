#!/usr/bin/env python
# encoding: utf-8
"""
insert_intervals.py

Created by Shengwei on 2014-07-07.
"""

# https://oj.leetcode.com/problems/insert-interval/
# tags: medium, array, interval, pointer, edge cases

"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
"""

# https://gist.github.com/senvey/772e0afd345934cee475

# note: sorting isn't actually required

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        copy = []
        
        index = 0
        while (index < len(intervals) and
                newInterval.start > intervals[index].end):
            # no overlap; copy directly and continue
            copy.append(intervals[index])
            index += 1
        
        if (index < len(intervals) and
                newInterval.start > intervals[index].start):
            # newInterval.start <= intervals[index].end
            newInterval.start = intervals[index].start
        
        while (index < len(intervals) and
                newInterval.end >= intervals[index].end):
            # skip intervals within newInterval
            index += 1
        
        if (index < len(intervals) and
                newInterval.end >= intervals[index].start):
            # also newInterval.end < intervals[index].end
            newInterval.end = intervals[index].end
            # skip current interval, i.e., intervals[index]
            index += 1
        
        copy.append(newInterval)
        
        while index < len(intervals):
            copy.append(intervals[index])
            index += 1
        
        return copy
