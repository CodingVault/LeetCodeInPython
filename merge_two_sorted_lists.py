#!/usr/bin/env python
# encoding: utf-8
"""
merge_two_sorted_lists.py

Created by  on 2014-07-21.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/merge-two-sorted-lists/
# tags: easy, linked-list, merge, sorted

"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        cursor = dummy_head = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cursor.next = l1
                l1 = l1.next
            else:
                cursor.next = l2
                l2 = l2.next
            cursor = cursor.next
        cursor.next = l1 or l2
        return dummy_head.next