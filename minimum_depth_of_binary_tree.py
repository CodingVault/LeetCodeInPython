#!/usr/bin/env python
# encoding: utf-8
"""
minimum_depth_of_binary_tree.py

Created by  on 2014-07-19.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/minimum-depth-of-binary-tree/
# tags: easy, tree, bfs, level-order

"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root is None:
            return 0
        
        depth = 1
        queue = [root, None]
        while queue:
            node = queue.pop(0)
            if node is None:
                if queue:
                    # note: do not increase depth if queue
                    #   is empty; otherwise the last return
                    #   result will be off by one
                    depth += 1
                    queue.append(None)
                
                # note: continue anyway if node is None,
                #   this covers when queue is empty
                continue
            
            if not node.left and not node.right:
                # leaf node
                return depth
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return depth