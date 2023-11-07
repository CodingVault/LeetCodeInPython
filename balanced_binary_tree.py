#!/usr/bin/env python
# encoding: utf-8
"""
balanced_binary_tree.py

Created by Shengwei on 2014-07-02.
"""

# https://oj.leetcode.com/problems/balanced-binary-tree/
# tags: medium, tree, dfs

"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""

# https://oj.leetcode.com/discuss/3931/can-we-have-a-better-solution

# note: there could be different definition of balanced tree
# https://oj.leetcode.com/discuss/59/different-definitions-balanced-result-different-judgments

def check_balance(node):
    """Retrun -1 if unbalanced; if balanced, return the depth
    """
    if node == None:
        return 0
    
    left_depth = check_balance(node.left)
    if left_depth == -1:
        return -1
    right_depth = check_balance(node.right)
    if right_depth == -1:
        return -1
    
    if abs(left_depth - right_depth) <= 1:
        return 1 + max(left_depth, right_depth)
    return -1
    

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        return check_balance(root) >= 0
