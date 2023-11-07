#!/usr/bin/env python
# encoding: utf-8
"""
flatten_binary_tree.py

Created by Shengwei on 2014-07-02.
"""

# https://oj.leetcode.com/problems/flatten-binary-tree-to-linked-list/
# tags: medium, tree, linked-list, recursion, preorder, dfs

"""
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6

"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

############# preorder dfs #############
class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root is None:
            return
        
        stack = [root]
        pre = TreeNode(0)
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            
            pre.left = None
            pre.right = node
            pre = node

############# recursion #############
class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root is None:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        if root.left is None:
            return

        pre = root.left
        while pre.right:
            pre = pre.right
        pre.right = root.right
        root.right = root.left
        root.left = None
