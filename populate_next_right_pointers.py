#!/usr/bin/env python
# encoding: utf-8
"""
populate_next_right_pointers.py

Created by Shengwei on 2014-07-27.
"""

# https://oj.leetcode.com/problems/populating-next-right-pointers-in-each-node/
# tags: medium, tree, pointer, recursion

"""Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
"""

# https://oj.leetcode.com/discuss/1808/may-only-constant-extra-space-does-mean-cannot-use-recursion

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        
        head = root
        while head.left:
            parent = head
            cursor = None
            while parent:
                if cursor:
                    cursor.next = parent.left
                parent.left.next = parent.right
                cursor = parent.right
                parent = parent.next
            head = head.left
