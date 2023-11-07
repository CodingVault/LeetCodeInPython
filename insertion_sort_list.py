#!/usr/bin/env python
# encoding: utf-8
"""
insertion_sort_list.py

Created by Shengwei on 2014-07-26.
"""

# https://oj.leetcode.com/problems/insertion-sort-list/
# tags: medium, linked-list, sort, edge cases, optimization

"""
Sort a linked list using insertion sort.
"""

# https://oj.leetcode.com/discuss/7482/one-way-to-accept-in-python-against-tle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        """Sort the list with insertion sort strategy.
        
        `cursor` points at one node prior to the one that
        is being processed; `pre` travels from dummy_head
        to `cursor`, finding the place to insert the node.
        """
        pre = cursor = dummy_head = ListNode(0)
        dummy_head.next = head
    
        while cursor.next:
            # note: only reset `pre` when `pre.next` is greater than
            #   the node to be processed, which means the insertion
            #   point could be before `pre`.
            if pre.next.val > cursor.next.val:
                pre = dummy_head
        
            while pre.next.val < cursor.next.val:
                pre = pre.next
            
            if pre != cursor:
                node = cursor.next
                cursor.next = node.next
                node.next = pre.next
                pre.next = node
            else:
                cursor = cursor.next
    
        return dummy_head.next

############## TLE ##############
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        cursor = dummy_head = ListNode(0)
        dummy_head.next = head
        
        while cursor.next:
            pre = dummy_head
            while pre.next.val < cursor.next.val:
                pre = pre.next
                
            if pre != cursor:
                node = cursor.next
                cursor.next = node.next
                node.next = pre.next
                pre.next = node
            else:
                cursor = cursor.next
        
        return dummy_head.next
