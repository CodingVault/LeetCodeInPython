#!/usr/bin/env python
# encoding: utf-8
"""
1353. Maximum Number of Events That Can Be Attended 

Created by Shengwei on 2022-04-18.
"""

# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/
# tags: medium, array, interval, heap

"""
You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.

Return the maximum number of events you can attend.


Example 1:

Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.

Example 2:

Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4
 

Constraints:

1 <= events.length <= 105
events[i].length == 2
1 <= startDayi <= endDayi <= 105
"""

# https://www.1point3acres.com/bbs/thread-885226-1-1.html (FB)

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """Loop through all the events:
        1. if no ongoing meeting now, move current day to the start day of the next earliest meeting
        2. for all the meetings start from the current day, add end days to the priority queue
        3. 1) attend the meeting that ends the earliest if any meeting is ongoing (res += 1),
           2) remove end days in the queue that have ended by the current day
        4. move the current day to the next, and repeat
        """
        
        if not events:
            return 0
        
        import heapq
        
        sorted_events = sorted(events)
        res = 0
        curr = 1
        end_days = []
        index = 0
        while index < len(events) or end_days:
            if not end_days and curr <= sorted_events[index][0]:
                curr = sorted_events[index][0]
            
            while index < len(events) and sorted_events[index][0] <= curr:  # "<=" can be "=="
                heapq.heappush(end_days, sorted_events[index][1])
                index += 1
            
            if end_days:  # no need to check because of the first "if" in the loop
                heapq.heappop(end_days)
                res += 1
                
            while end_days and curr >= end_days[0]:
                heapq.heappop(end_days)
            
            curr += 1  # move this up so no need to check "=" for the loop above
        
        return res


# slight improvements
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """Loop through all the events:
        1. if no ongoing meeting now, move current day to the start day of the next earliest meeting
        2. for all the meetings start from the current day, add end days to the priority queue
        3. 1) attend the meeting that ends the earliest if any meeting is ongoing (res += 1),
           2) remove end days in the queue that have ended by the current day
        4. move the current day to the next, and repeat
        """
        
        if not events:
            return 0
        
        import heapq
        
        events.sort()
        res = 0
        curr = 1
        end_days = []
        index, size = 0, len(events)
        while index < size or end_days:
            if not end_days and curr <= events[index][0]:
                curr = events[index][0]
            
            while index < size and events[index][0] == curr:
                heapq.heappush(end_days, events[index][1])
                index += 1
            
            heapq.heappop(end_days)
            res += 1
            curr += 1
                
            while end_days and curr > end_days[0]:
                heapq.heappop(end_days)
        
        return res
