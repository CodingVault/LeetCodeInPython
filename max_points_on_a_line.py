#!/usr/bin/env python
# encoding: utf-8
"""
max_points_on_a_line.py

Created by Shengwei on 2014-08-03.
"""

# https://oj.leetcode.com/problems/max-points-on-a-line/
# tags: hard, array, points, dups

"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
"""

# https://oj.leetcode.com/discuss/1472/have-accepted-solution-feel-terrible-about-what-others-think

# reverse the scan from right to left
# https://oj.leetcode.com/discuss/7607/accepted-code-in-python

# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        def line(p1, p2):
            """It's important to make sure:
                line(p1, p2) == line(p2, p1)
            """
            
            if p1.x == p2.x:
                # vertical line
                return (1, 0, p1.x)
            
            if p1.y == p2.y:
                # horizontal line
                return (0, 1, p1.y)
            
            g = gcd(p2.y - p1.y, p2.x - p1.x)
            a = (p2.y - p1.y) / g
            b = (p2.x - p1.x) / g
            # gcd(4, -6) == -2, gcd(-4, 6) == 2, so
            # if a * b < 0, then a < 0 and b > 0
            c = p1.y * b - p1.x * a
            return (a, b, c)
        
        cache = {}
        p_counts = collections.defaultdict(int)
        for i, new_point in enumerate(points):
            p_counts[(new_point.x, new_point.y)] += 1
            slopes = set()
            for prior_point in points[:i]:
                if (new_point.x == prior_point.x and
                        new_point.y == prior_point.y):
                    continue
                
                slope = line(new_point, prior_point)
                slopes.add(slope)
                
                # if there are multiple duplicate points before
                # current point, the default count of points on
                # the line would be the number of dups; for dups
                # after current point, they will be counted
                # correctly as they are also on the same slope
                count = p_counts[(prior_point.x, prior_point.y)]
                cache.setdefault(slope, count)
            
            # for each new point on each slope, count only once
            for slope in slopes:
                cache[slope] += 1
        
        if cache:
            return max(cache.values())
        return len(points)
