#!/usr/bin/env python
# encoding: utf-8
"""
linked_list_cycle.py

Created by  on 2014-06-30.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/linked-list-cycle/

"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head is None:
            return False

        visited = set()
        while head.next is not None:
            if head.next in visited:
                return True
            visited.add(head)
            head = head.next
        return False


