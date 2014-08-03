#!/usr/bin/env python
# encoding: utf-8
"""
triangle.py

Created by Shengwei on 2014-07-03.
"""

# https://oj.leetcode.com/problems/triangle/

"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""

# https://oj.leetcode.com/discuss/1486/can-i-modify-the-triangle

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        """Think about the triangle as a graph similar to a tree,
        with nodes as the numbers in the triangle, and edges connecting
        to "adjacent" numbers. From top down, we may treat their
        relationship as parents and children, where some nodes can have
        two parents, such as 5 in the given example (it has 3 and 4 as
        parents).

        Starting from the second level (the level with 2 elements),
        computes the min value it could be at triangle[i][j] by
         - add up triangle[i][j] with it's parents, respectively
         - get the min value of two sums
        and then replace triangle[i][j] with the min value.
        (for triangle[i][j], its parents could be triangle[i-1][j-1],
        and triangle[i-1][j]; while sometimes there is only one parent)
        
        By interatively doing this, the parents hold the sum of min
        path from them up to the "root" element.
        """
        if triangle is None or len(triangle) == 0:
            return
        
        if len(triangle) == 1:
            return triangle[0][0]
        
        for level in xrange(1, len(triangle)):
            # current level to update the sum of min path
            cur_level = triangle[level]
            upper_level = triangle[level - 1]
            
            for index in xrange(len(cur_level)):
                
                # for left most number of each level, it has no left
                # parent, so the sum is only to add with righ parent
                if index == 0:
                    cur_level[index] += upper_level[0]
                
                # for right most number of each level, it has no right
                # parent, so the sum is only to add with left parent
                elif index == len(upper_level):
                    cur_level[index] += upper_level[index - 1]
                
                # otherwise, there are two parents
                else:
                    cur_level[index] = min(
                        cur_level[index] + upper_level[index - 1],
                        cur_level[index] + upper_level[index]
                    )
        
        # the last level eventually holds min values of all paths
        return min(triangle[-1])
