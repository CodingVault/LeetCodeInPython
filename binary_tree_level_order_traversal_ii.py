#!/usr/bin/env python
# encoding: utf-8
"""
binary_tree_level_order_traversal_ii.py

Created by  on 2014-07-29.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/binary-tree-level-order-traversal-ii/
# tags: medium, tree, traversal, reversed, bfs

"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""

# https://oj.leetcode.com/discuss/5353/there-better-regular-level-order-traversal-reverse-result

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if root is None:
            return []
        
        # the first None as a sentinel so the root
        # level will be added to the result
        stack = [None, root]
        index = 0
        while index < len(stack):
            node = stack[index]
            if node is None:
                if index == len(stack) - 1:
                    break
                stack.append(None)
            
            else:
                # add children in reversed order
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            
            # remember to increase index even when
            # the node is None
            index += 1
        
        result, level = [], []
        stack.pop()  # remove the last None marker
        while stack:
            if stack[-1] is None:
                # processed one level
                result.append(level)
                level = []
                stack.pop()  # pop out None marker
                continue
            level.append(stack.pop().val)
            
        return result

############## alternative ##############
class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if root is None:
            return []

        stack, index = [root, None], 0
        while index < len(stack):
            node = stack[index]
            if node is None:
                if index == len(stack) - 1:
                    break
                stack.append(None)

            else:
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

            # remember to increase index even when
            # the node is None
            index += 1

        result = []
        start = end = -1  # end always points at None
        while end > -len(stack):
            while start > -len(stack) and stack[start - 1]:
                # stack[start - 1], if exists, is not None
                start -= 1
            # start == -len(stack) or stack[start - 1] is None
            level = [node.val for node in stack[start:end]]
            result.append(level)
            # more exactly, start can be start - 2 now
            start = end = start - 1

        return result
