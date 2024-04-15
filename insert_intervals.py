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


# 20240411
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals
        
        # note: edge cases if new interval is greater or smaller than all existing ones
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        if newInterval[0] > intervals[-1][1]:
            return intervals + [newInterval]

        begins, ends = [], []
        begin = end = None
        for interval in intervals:
            if interval[1] < newInterval[0]:
                begins.append(interval[0])
                ends.append(interval[1])
            elif interval[0] > newInterval[1]:
                if newInterval[0] > ends[-1]:
                    # note: edge case when there is no overlap for new interval
                    begins.append(newInterval[0])
                    ends.append(newInterval[1])
                begins.append(interval[0])
                ends.append(interval[1])
            else:
                if begin is None:
                    begin = min(interval[0], newInterval[0])
                    begins.append(begin)
                else:
                    begins[-1] = min(begins[-1], interval[0])

                if end is None:
                    end = max(interval[1], newInterval[1])
                    ends.append(end)
                else:
                    ends[-1] = max(ends[-1], interval[1])

        return list(zip(begins, ends))

# alternative / reversed if..else
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals
        
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        if newInterval[0] > intervals[-1][1]:
            return intervals + [newInterval]

        begins, ends = [], []
        begin = end = None
        for interval in intervals:
            if interval[1] >= newInterval[0] and interval[0] <= newInterval[1]:
                if begin is None:
                    begin = min(interval[0], newInterval[0])
                    begins.append(begin)
                else:
                    begins[-1] = min(begins[-1], interval[0])

                if end is None:
                    end = max(interval[1], newInterval[1])
                    ends.append(end)
                else:
                    ends[-1] = max(ends[-1], interval[1])
            else:
                if interval[0] > newInterval[1] and newInterval[0] > ends[-1]:
                    begins.append(newInterval[0])
                    ends.append(newInterval[1])
                begins.append(interval[0])
                ends.append(interval[1])

        return list(zip(begins, ends))




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
