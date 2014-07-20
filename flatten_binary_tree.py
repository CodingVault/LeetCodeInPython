#!/usr/bin/env python
# encoding: utf-8
"""
flatten_binary_tree.py

Created by  on 2014-07-02.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/flatten-binary-tree-to-linked-list/

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


def flat(root):
    if root is None:
        return

    flat(root.left)
    flat(root.right)
    
    if root.left is None:
        return

    pre = root.left
    while pre.right is not None:
        pre = pre.right
    pre.right = root.right
    root.right = root.left
    
    # important!
    root.left = None
    

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        flat(root)