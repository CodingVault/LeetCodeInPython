#!/usr/bin/env python
# encoding: utf-8
"""
partition_list.py

Created by  on 2014-07-15.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/partition-list/

"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if head is None or head.next is None:
            return head
        
        dummy_head = ListNode(0)
        dummy_head.next = head
        left_head = right_head = dummy_head
        left_tail = right_tail = dummy_head
        cursor = dummy_head
        
        while cursor.next:
            cursor = cursor.next
            if cursor.val < x:
                if left_head == dummy_head:
                    left_head = cursor
                left_tail.next = cursor
                left_tail = cursor
            else:
                if right_head == dummy_head:
                    right_head = cursor
                right_tail.next = cursor
                right_tail = cursor
        
        if right_head == dummy_head:
            right_head = None
        left_tail.next = right_head
        right_tail.next = None
        
        if left_head == dummy_head:
            return right_head
        return left_head
