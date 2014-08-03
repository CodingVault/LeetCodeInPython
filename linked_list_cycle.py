#!/usr/bin/env python
# encoding: utf-8
"""
linked_list_cycle.py

Created by Shengwei on 2014-06-30.
"""

# https://oj.leetcode.com/problems/linked-list-cycle/
# tags: easy, linked-list, hashtable

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

############ no extra space ############
class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head is None:
            return False

        walker, runner = head, head.next
        while runner and runner.next:
            if walker == runner:
                return True
            
            walker = walker.next
            runner = runner.next.next
        
        return False

# and better:

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        walker, runner = head, head
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                return True
        return False


############ hashtable ############
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


