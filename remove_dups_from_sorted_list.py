#!/usr/bin/env python
# encoding: utf-8
"""
remove_dups_from_sorted_list.py

Created by Shengwei on 2014-07-05.
"""

# https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list/
# tags: easy, linked-list, pointer, dups

"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

############# V2 #############
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        cursor = head
        while cursor and cursor.next:
            if cursor.val == cursor.next.val:
                cursor.next = cursor.next.next
            else:
                cursor = cursor.next
        return head

############# V1 #############
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
        
        walker, runner = head, head.next
        while runner:
            if walker.val != runner.val:
                walker.next = runner
                walker = runner
            
            runner = runner.next
        
        # IMPORTANT! truncate the linked list just in case
        # test case: {1, 1} -> {1}
        walker.next = None
        
        return head
