#!/usr/bin/env python
# encoding: utf-8
"""
253. Meeting Rooms II

Created by Shengwei on 2022-04-21.
"""

# locked
# tags: medium, array, interval, heap

"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.


"""

class Solution:
  def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    import heapq

    end_heap = []
    for start, end in sorted(intervals):
        # if there is "at least one" meeting that has ended prior to current meeting,
        # pop it out to reuse the meeting room;
        # don't bother other meetings and let the meeting rooms be occupied,
        # so it's easier to count how many rooms needed at maximum
        if end_heap and start > end_heap[0]:
            heapq.heappop(end_heap)
        heapq.heappush(end_heap, end)

    return len(end_heap)
