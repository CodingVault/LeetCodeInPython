#!/usr/bin/env python
# encoding: utf-8
"""
remove_nth_node_from_end_of_list.py

Created by  on 2014-07-15.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/remove-nth-node-from-end-of-list/
# tags: medium, linked-list, pointer, edge cases, dummy head

"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

############# with dummy head #############
class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if head is None:
            return None

        front = head
        for _ in xrange(n):
            front = front.next
        
        follower = dummy_head = ListNode(0)
        follower.next = head
        while front:
            front = front.next
            follower = follower.next
        
        follower.next = follower.next.next
        return dummy_head.next


############# V1 #############
class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if head is None:
            return head

        tail = head
        for i in xrange(n):
            if tail.next:
                tail = tail.next
            else:
                if i == n - 1:
                    head = head.next
                return head
        
        # pre points at the element right before
        # the one should be removed, and pre is
        # n elements previous to tail
        pre = head
        while tail.next:
            tail = tail.next
            pre = pre.next
        
        pre.next = pre.next.next
        return head
