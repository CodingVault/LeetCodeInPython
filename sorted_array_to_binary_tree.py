#!/usr/bin/env python
# encoding: utf-8
"""
sorted_array_to_binary_tree.py

Created by Shengwei on 2014-07-03.
"""

# https://oj.leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# tags: easy, tree, array, sorted, convert, D&C

"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        
        def convert_array(left, right):
            """Convert num[left:right] to a (sub)tree."""
            
            # num[x:x] is an empty list (x can be any number)
            if left >= right:
                return None
            
            # mid point at the very middle of num[left:right]
            # or the right one of the middle two
            mid = (left + right) / 2

            root = TreeNode(num[mid])
            root.left = convert_array(left, mid)
            root.right = convert_array(mid + 1, right)

            return root
        
        return convert_array(0, len(num))
