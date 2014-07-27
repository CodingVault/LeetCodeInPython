#!/usr/bin/env python
# encoding: utf-8
"""
reorder_list.py

Created by  on 2014-07-26.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/reorder-list/
# tags: medium, linked-list, edge cases, reverse

"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
"""

# https://oj.leetcode.com/discuss/236/does-this-problem-solution-time-complexity-space-comlexity
# note: if walker and runner are initialized with head, it will also work; in this case,
#   an even-length list will be split into unequal parts, but the middle two nodes of the
#   original list do not need to change, i.e., with {1,2,3} and {4}, it still gives correct
#   answer; in fact, this saves one slicing it requires if it splits equally as {1,2} and {4,3}.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        walker = runner = dummy_head = ListNode(0)
        dummy_head.next = head
        
        # find the very middle or the left one of
        # middle two nodes with walker pointing it
        while runner and runner.next:
            runner = runner.next.next
            walker = walker.next
        
        # break the list into two parts, and
        # reverse the second half of the list
        cursor = walker.next
        walker.next = pre = None
        while cursor:
            post = cursor.next
            cursor.next = pre
            pre = cursor
            cursor = post
        
        # splice the two parts together
        cursor = dummy_head
        left, right = head, pre
        while left and right:
            cursor.next = left
            left = left.next
            cursor = cursor.next
            cursor.next = right
            right = right.next
            cursor = cursor.next
        # note: remember to link the last node
        #   in the left half in case there are
        #   odd number of nodes in total
        cursor.next = left
        
        return dummy_head.next
