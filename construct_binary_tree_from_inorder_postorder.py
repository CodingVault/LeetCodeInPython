#!/usr/bin/env python
# encoding: utf-8
"""
construct_binary_tree_from_inorder_postorder.py

Created by  on 2014-07-19.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# tags: easy, tree, traversal, recursion

"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""

# TODO: do it iteratively instead of recursively
# also: https://oj.leetcode.com/discuss/7245/here-is-my-log-solution-is-there-any-better-solution-accepted

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if len(inorder) == 0:
            return None
        
        root = TreeNode(postorder[-1])
        root_index = inorder.index(root.val)
        root.left = self.buildTree(inorder[:root_index], postorder[:root_index])
        root.right = self.buildTree(inorder[root_index+1:], postorder[root_index:-1])
        
        return root