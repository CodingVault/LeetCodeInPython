#!/usr/bin/env python
# encoding: utf-8
"""
binary_tree_preorder.py

Created by Shengwei on 2014-06-30.
"""

# https://oj.leetcode.com/problems/binary-tree-preorder-traversal/
# tags: easy, tree, traversal, dfs

"""
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 20240329
def preorder(root):
    cur, stack = root, []
    while stack or cur:
        if cur:
            print(cur.value)
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop().right


class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        if root is None:
            return []

        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)

            # note: right first!
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return res

