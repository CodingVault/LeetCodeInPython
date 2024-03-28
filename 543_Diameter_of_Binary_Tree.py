#!/usr/bin/env python
# encoding: utf-8
"""
543. Diameter of Binary Tree

Created by Shengwei on 2023-10-06.

Used:
* Meta: https://www.1point3acres.com/bbs/thread-1026007-1-1.html
"""

# https://leetcode.com/problems/diameter-of-binary-tree/description/
# tags: easy / medium, tree, recursion

"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def check(node):
            if not node:
                return 0, 0
            
            left_length, left_diameter = check(node.left)
            right_length, right_diameter = check(node.right)
            current_diameter = left_length + right_length

            return (max(left_length, right_length) + 1,
                max(left_diameter, right_diameter, current_diameter))
        
        return check(root)[1]


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def check(node):
            if not node.left and not node.right:
                return 1, 0
            
            if node.left:
                left_length, left_diameter = check(node.left)
            else:
                left_length = left_diameter = 0

            if node.right:
                right_length, right_diameter = check(node.right)
            else:
                right_length = right_diameter = 0

            current_diameter = left_length + right_length

            return (max(left_length, right_length) + 1,
                max(left_diameter, right_diameter, current_diameter))
        
        return check(root)[1]