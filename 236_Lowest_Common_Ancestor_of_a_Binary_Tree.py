#!/usr/bin/env python
# encoding: utf-8
"""
236. Lowest Common Ancestor of a Binary Tree

Created by Shengwei on 2022-04-17.
"""

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# tags: easy / medium, tree, recursion

"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1
"""

# 2023-10-28
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        def routine(node: 'TreeNode') -> 'TreeNode':
            # note: this can be optimized to check if input node is None
            res_left = routine(node.left) if node.left else None
            if res_left and res_left not in (p, q):
                return res_left

            res_right = routine(node.right) if node.right else None
            if res_right and res_right not in (p, q):
                return res_right

            if res_left and res_right:
                return node
            
            # note: this can be moved above to the beginning
            if node in (p, q):
                return node
            
            return res_left or res_right
            
        return routine(root)


# 2022/04 (too many edge cases, better to use the earlier one)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """Finds the least common ancestor of node1 and node2 in the tree of given root.

        Returns:
            - None if not found
            - root if 1. each of (node1, node2) found in root's left and right subtrees
                or 2. one of (node1, node2) found in root's children and root is the another
            - another node returned from root's left or right subtrees, as it's found earlier
            - node1 or node2 if only one node is found in the tree of given root
        """
        if root is None:
            return

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # print("node:", root, "left:", left, "right:", right)
        all_set = (left, right, root)
        if p in all_set and q in all_set:
            return root

        def is_parent_node(node):
            return node and node != p and node != q

        if is_parent_node(left):
            return left
        if is_parent_node(right):
            return right

        def check(node):
            if node in (p, q):
                return node

        return check(left) or check(right) or check(root)


# 2019/11
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def check(node: 'TreeNode') -> 'TreeNode':
            if not node:
                return
            if node == p or node == q:
                return node
            
            left, right = check(node.left), check(node.right)
            if left and right:
                return node
            
            return left or right
        
        return check(root)
