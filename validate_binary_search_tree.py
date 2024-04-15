#!/usr/bin/env python
# encoding: utf-8
"""
validate_binary_search_tree.py

Created by Shengwei on 2014-07-04.
"""

# https://oj.leetcode.com/problems/validate-binary-search-tree/

"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""

# https://oj.leetcode.com/discuss/281/how-solve-this-problem-validate-binary-search-tree-iterative
# for binary search tree, the inorder sequence is monotonically ascending;
# further, each level is also monotonically ascending

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        
        def check(node, min_val, max_val):
            if node is None:
                return True
            
            left, right = node.left, node.right
            if left and (left.val >= node.val or left.val <= min_val):
                return False
            if right and (right.val <= node.val or right.val >= max_val):
                return False
            
            return (check(left, min_val, node.val) and
                    check(right, node.val, max_val))
        
        # alternative: return check(root, -sys.maxint - 1, sys.maxint)
        # Py3: sys.maxsize
        return check(root, -9223372036854775808, 9223372036854775807)
