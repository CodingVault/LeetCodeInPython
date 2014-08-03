#!/usr/bin/env python
# encoding: utf-8
"""
symmetric_tree.py

Created by Shengwei on 2014-07-04.
"""

# https://oj.leetcode.com/problems/symmetric-tree/
# tags: medium, tree, recursion

"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
"""

# TODO: use iterative approach instead of recusive one
# https://oj.leetcode.com/discuss/456/recusive-solution-symmetric-optimal-solution-inordertraversal

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        
        if root is None:
            return True
        
        def check_symmetry(left, right):
            if left is None and right is None:
                return True
            if not left or not right or left.val != right.val:
                return False
            
            return (
                check_symmetry(left.left, right.right) and
                check_symmetry(left.right, right.left)
            )
        
        return check_symmetry(root.left, root.right)
