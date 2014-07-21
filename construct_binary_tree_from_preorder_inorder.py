#!/usr/bin/env python
# encoding: utf-8
"""
construct_binary_tree_from_preorder_inorder.py

Created by  on 2014-07-20.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# tags: easy, tree, traversal, recursion

"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""

# bug note: didn't calculate distance but used index directly for preorder

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        """Avoid copying sub-arrays but manipulate index and reuse
        the pass-in arguments -- reduce space complexity.
        """
        
        def build(p_start, p_end, i_start, i_end):
            if i_start > i_end:
                return None
            
            root = TreeNode(preorder[p_start])
            index = inorder.index(root.val, i_start)
            distance = index - i_start
            root.left = build(p_start+1, p_start+distance, i_start, index-1)
            root.right = build(p_start+distance+1, p_end, index+1, i_end)
            
            return root
        
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
