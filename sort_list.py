#!/usr/bin/env python
# encoding: utf-8
"""
sort_list.py

Created by  on 2014-07-21.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/sort-list/
# tags: easy / medium, linked-list, merge sort, recursion

"""
Sort a linked list in O(n log n) time using constant space complexity.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def merge_sorted_list(l1, l2):
    cursor = dummy_head = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cursor.next = l1
            l1 = l1.next
        else:
            cursor.next = l2
            l2 = l2.next
    
        # bug: forgot this... what a shame!
        cursor = cursor.next
    
    cursor.next = l1 or l2
    return dummy_head.next

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        cur, count = head, 0
        while cur:
            count += 1
            cur = cur.next
        
        def sort(head, length):
            if length <= 1:
                if head:
                    # IMPORTANT: break nodes into individuals.
                    # There could otherwise exist a cycle.
                    head.next = None
                return head
            
            l2, half = head, length / 2
            for _ in xrange(half):
                l2 = l2.next
            
            # note: neither l1 nor l2 can be None
            l1 = sort(head, half)
            l2 = sort(l2, length - half)
            return merge_sorted_list(l1, l2)
        
        return sort(head, count)
