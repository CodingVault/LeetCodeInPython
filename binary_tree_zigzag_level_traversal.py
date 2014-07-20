#!/usr/bin/env python
# encoding: utf-8
"""
binary_tree_zigzag_level_traversal.py

Created by  on 2014-07-15.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        
        res = []
        odd_stack, even_stack = [root], []
        
        while odd_stack or even_stack:
            
            nodes = []
            while odd_stack:
                node = odd_stack.pop()
                nodes.append(node.val)
                if node.left:
                    even_stack.append(node.left)
                if node.right:
                    even_stack.append(node.right)
            if nodes:
                res.append(nodes)
            
            nodes = []
            while even_stack:
                node = even_stack.pop()
                nodes.append(node.val)
                if node.right:
                    odd_stack.append(node.right)
                if node.left:
                    odd_stack.append(node.left)
            if nodes:
                res.append(nodes)
        
        return res