#!/usr/bin/env python
# encoding: utf-8
"""
same_tree.py

Created by  on 2014-07-15.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/same-tree/
# tags: easy, tree, recursion

"""
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        
        if not p or not q or p.val != q.val:
            return False
        
        return (
            self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right)
        )