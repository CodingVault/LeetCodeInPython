#!/usr/bin/env python
# encoding: utf-8
"""
230. Kth Smallest Element in a BST

Created by Shengwei on 2022-04-25.
"""

# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# tags: easy / medium, tree, inorder, kth

"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 
Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cursor = root
        stack = []
        while cursor or stack:
            if cursor:
                stack.append(cursor)
                cursor = cursor.left
            else:
                node = stack.pop()
                k -= 1
                if not k:
                    return node.val
                cursor = node.right
        return -1
