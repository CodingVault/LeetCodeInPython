#!/usr/bin/env python
# encoding: utf-8
"""
merge_k_sorted_lists.py

Created by Shengwei on 2014-07-21.
"""

# https://oj.leetcode.com/problems/merge-k-sorted-lists/
# tags: easy / medium, linked-list, sorted, merge, D&C, recursion

"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
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
        cursor = cursor.next
    cursor.next = l1 or l2
    return dummy_head.next

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        
        def sub_merge(left, right):
            mid = (left + right) / 2
            
            if right - left == 1:
                # mid == left
                return lists[left]
            
            l1 = sub_merge(left, mid)
            l2 = sub_merge(mid, right)
            return merge_sorted_list(l1, l2)
        
        return sub_merge(0, len(lists))


########## brute force ##########

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        
        head = lists[0]
        for index in xrange(1, len(lists)):
            head = merge_sorted_list(head, lists[index])
        return head
