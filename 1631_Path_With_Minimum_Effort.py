#!/usr/bin/env python
# encoding: utf-8
"""
1631. Path With Minimum Effort

Created by Shengwei on 2024-06-23.

Used:
- Snap: https://www.1point3acres.com/bbs/thread-1047384-1-1.html
"""

# https://leetcode.com/problems/path-with-minimum-effort/description/
# tags: medium / hard, matrix, max, min, Dijikstra

"""
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

 

Example 1:

Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

Example 2:

Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].

Example 3:

Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.
 

Constraints:

rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106
"""

# https://leetcode.com/problems/path-with-minimum-effort/solutions/909017/java-python-dijikstra-binary-search-clean-concise/
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        from heapq import heappush as push
        from heapq import heappop as pop
        from math import inf

        if not heights: return 0

        m, n = len(heights), len(heights[0])
        cur_efforts = [(0, (0, 0))]  # effort, (x, y)
        # min efforts so far, may not be the global min, to save extra push
        min_efforts = {}  # key: (x, y), value: min_effort
        direction = (0, 1, 0, -1, 0)

        while cur_efforts:
            effort, (x, y) = pop(cur_efforts)
            # skip if has processed (x, y) with smaller effort
            # note: in this case, cannot skip effort with the same effort as added earlier
            if effort > min_efforts.get((x, y), inf): continue
            if (x, y) == (m - 1, n - 1):
                return effort
            
            for xd, yd in zip(direction, direction[1:]):
                nx, ny = x + xd, y + yd
                if 0 <= nx < m and 0 <= ny < n:
                    n_effort = max(effort, abs(heights[x][y] - heights[nx][ny]))
                    # track currently min effort for (nx, ny) so far, even if it's not the global min yet
                    if n_effort < min_efforts.get((nx, ny), inf):
                        min_efforts[(nx, ny)] = n_effort
                        push(cur_efforts, (n_effort, (nx, ny)))
        
        # should never be here
        return -1

# comparison
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        from heapq import heappush as push
        from heapq import heappop as pop
        from math import inf

        if not heights: return 0

        m, n = len(heights), len(heights[0])
        cur_efforts = [(0, (0, 0))]  # effort, (x, y)
        min_efforts = {}  # use this to track global min only
        direction = (0, 1, 0, -1, 0)

        while cur_efforts:
            effort, (x, y) = pop(cur_efforts)
            # skip if has processed (x, y) with equal or smaller effort
            if effort >= min_efforts.get((x, y), inf): continue
            if (x, y) == (m - 1, n - 1):
                return effort
            # this effort must be the global min now
            min_efforts[(x, y)] = effort
            
            for xd, yd in zip(direction, direction[1:]):
                nx, ny = x + xd, y + yd
                if 0 <= nx < m and 0 <= ny < n:
                    n_effort = max(effort, abs(heights[x][y] - heights[nx][ny]))
                    # theoretically no check here also works, but waste space and time
                    if n_effort < min_efforts.get((nx, ny), inf):
                        push(cur_efforts, (n_effort, (nx, ny)))
        
        return -1
