#!/usr/bin/env python
# encoding: utf-8
"""
linked_list_cycle_ii.py

Created by  on 2014-06-30.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/linked-list-cycle-ii/
# tags: medium, linked-list, logic

"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Follow up:
Can you solve it without using extra space?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

############ V2 ############
class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head is None or head.next is None:
            return
        walker, runner = head, head
        
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next
            if runner == walker:
                break
        if runner != walker:
            return

        walker = head
        while runner != walker:
            runner = runner.next
            walker = walker.next
        return walker

############ V1 ############
class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head is None:
            return None
        walker = head.next
        if walker is None:
            return None
        runner = head.next.next

        while runner != walker:
            if runner is None or runner.next is None:
                return None
            runner = runner.next.next
            walker = walker.next

        walker = head
        while runner != walker:
            runner = runner.next
            walker = walker.next

        return walker
