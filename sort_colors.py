#!/usr/bin/env python
# encoding: utf-8
"""
sort_colors.py

Created by  on 2014-07-23.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/sort-colors/
# tags: easy / medium, array, pointers, logic, edge cases

"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
"""

# TODO: try alternative
#   1. red and white pointers in the beginning, while blue pointer in the end
#   2. scan through the array until white pointer meets blue pointer, and
#       a) move red to the beginning, or
#       b) move blue to the end

class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        r, w, b = 0, 1, 2
        red, white, blue = 0, 0, 0
        
        while blue < len(A):
            if A[blue] == r:
                # the sequence is important!
                # for example, red and while may point at the same
                # element when there is no white being scanned
                A[blue], A[white], A[red] = A[white], A[red], A[blue]
                red += 1
                white += 1
            elif A[blue] == w:
                A[white], A[blue] = A[blue], A[white]
                white += 1
            blue += 1
            
