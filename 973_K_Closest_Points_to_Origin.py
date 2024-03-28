#!/usr/bin/env python
# encoding: utf-8
"""
973. K Closest Points to Origin 

Created by Shengwei on 2022-04-21.
"""

# https://leetcode.com/problems/k-closest-points-to-origin/
# tags: medium, quicksort

"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 
Example 1:

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].


Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
"""

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if K >= len(points):
            return points

        array = [(x * x + y * y, x, y) for x, y in points]
        def qsort(l: int, r: int) -> int:
            pivot = array[l]
            while l < r:
                while array[r][0] >= pivot[0] and l < r:
                    r -= 1
                array[l] = array[r]
                while array[l][0] <= pivot[0] and l < r:
                    l += 1
                array[r] = array[l]
            array[l] = pivot
            return l

        left, right = 0, len(array) - 1
        while left < K:
            mid = qsort(left, right)
            if K > mid:
                left = mid + 1
            else:
                right = mid - 1
        return [[x, y] for _, x, y in array[:K]]
