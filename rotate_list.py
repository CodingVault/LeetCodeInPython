#!/usr/bin/env python
# encoding: utf-8
"""
rotate_list.py

Created by  on 2014-07-15.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/rotate-list/

"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head is None or head.next is None:
            return head

        for _ in xrange(k):
            before_tail = head
            while before_tail.next.next is not None:
                before_tail = before_tail.next

            before_tail.next.next = head
            head = before_tail.next
            before_tail.next = None
        
        return head