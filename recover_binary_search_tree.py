#!/usr/bin/env python
# encoding: utf-8
"""
recover_binary_search_tree.py

Created by Shengwei on 2014-07-30.
"""

# https://oj.leetcode.com/problems/recover-binary-search-tree/
# tags: medium / hard, tree, traversal, optimization, recursion, tricky

"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
"""

# https://oj.leetcode.com/discuss/7319/an-elegent-time-complexity-and-space-complexity-algorithm
# https://oj.leetcode.com/discuss/2103/how-can-the-space-complextity-be-better-than-log-n-with-stack

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        to_swap = []
        
        def locate_swapped(pre, node):
            if node is None:
                return pre
            
            pre = locate_swapped(pre, node.left)
            
            if pre and pre.val > node.val:
                if not to_swap:
                    to_swap.append(pre)
                    to_swap.append(node)
                to_swap[-1] = node
            
            return locate_swapped(node, node.right)
        
        locate_swapped(None, root)
        to_swap[0].val, to_swap[1].val = to_swap[1].val, to_swap[0].val
        
        return root
