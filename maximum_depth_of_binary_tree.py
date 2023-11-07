#!/usr/bin/env python
# encoding: utf-8
"""
maximum_depth_of_binary_tree.py

Created by Shengwei on 2014-07-15.
"""

# https://oj.leetcode.com/problems/maximum-depth-of-binary-tree/
# tags: easy, tree, dfs, bfs, level-order

"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

######### recursive #########

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        
        def max_depth(node):
            if node is None:
               return 0 
            return 1 + max(max_depth(node.left), max_depth(node.right))
        
        return max_depth(root)

######### iterative #########

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root is None:
            return 0

        depth = 1   # the depth traversal is working on
        queue = [root, None]
        while len(queue) > 1:
            node = queue.pop(0)
            if node is None:
                depth += 1
                queue.append(None)
                continue

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return depth
