#!/usr/bin/env python
# encoding: utf-8
"""
remove_dups_from_sorted_list_ii.py

Created by  on 2014-07-05.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# tags: medium, linked-list, pointer, dups, edge cases

"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""

# TODO: other solutions
# 1. use counter to distinguish the situation where current value is not the same as the next
#    if counter is 0, current node is unique; otherwise, start from the next node
#   changejian's code and https://oj.leetcode.com/discuss/5743/how-can-i-improve-my-code)
# 2. use two pointers, move prior one when necessary
#   https://github.com/MaskRay/LeetCode/blob/master/remove-duplicates-from-sorted-list-ii.cc


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None:
            return head
        
        pre = dummy_head = ListNode(0)
        dummy_head.next = head
        walker, runner = head, head.next
        
        while walker and walker.next:
            if walker.val != walker.next.val:
                pre.next = walker
                pre = walker
                walker = walker.next
            else:
                # look for next unique node or None
                runner = walker.next
                while runner.next and runner.next.val == walker.val:
                    runner = runner.next
                
                # runner.next can be either None or a node with different value
                walker = runner.next
        
        # walker is either None (last node is also a dup) or last unique node
        pre.next = walker
        
        return dummy_head.next
