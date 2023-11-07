#!/usr/bin/env python
# encoding: utf-8
"""
sort_list_to_binary_tree.py

Created by Shengwei on 2014-07-03.
"""

# https://oj.leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
# tags: easy, tree, linked-list, sorted, convert, D&C

"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        cur, total = head, 0
        while cur:
            total += 1
            cur = cur.next
        
        def convert_list(h, length):
            if length == 0:
                return None
            
            cur = h
            for _ in xrange(length / 2):
                cur = cur.next
            # cur points at the very middle or
            # the right one of middle two
            
            root = TreeNode(cur.val)
            root.left = convert_list(h, length / 2)
            root.right = convert_list(cur.next, length - length / 2 - 1)
            return root
        
        return convert_list(head, total)
            
            
