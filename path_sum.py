#!/usr/bin/env python
# encoding: utf-8
"""
path_sum.py

Created by Shengwei on 2014-07-19.
"""

# https://oj.leetcode.com/problems/path-sum/
# tags: easy, tree, dfs, sum

"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        
        stack = [(root, sum)]
        while stack:
            node, remainder = stack.pop()
            
            # leaf node: check remainder
            if not node.left and not node.right:
                if node.val == remainder:
                    return True
            
            remainder -= node.val
            if node.right:
                stack.append((node.right, remainder))
            if node.left:
                stack.append((node.left, remainder))
        
        return False
