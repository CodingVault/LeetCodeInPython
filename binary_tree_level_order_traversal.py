#!/usr/bin/env python
# encoding: utf-8
"""
binary_tree_level_order_traversal.py

Created by  on 2014-07-29.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/binary-tree-level-order-traversal/
# tags: easy, tree, traversal, bfs

"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
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
    def levelOrder(self, root):
        if root is None:
            return []
        
        def generator():
            queue = [root, None]
            level = []
            while queue:
                node = queue.pop(0)
                if node is None:
                    # yield the data before doing anything
                    yield level
                    level = []
                    
                    if not queue:
                        break
                    queue.append(None)
                    continue
                
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return list(generator())
