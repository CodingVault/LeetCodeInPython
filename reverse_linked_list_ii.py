#!/usr/bin/env python
# encoding: utf-8
"""
reverse_linked_list_ii.py

Created by  on 2014-07-25.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/reverse-linked-list-ii/
# tags: medium, linked-list, pointer, dummy head, edge cases, reverse

"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        
        cursor = dummy_head = ListNode(0)
        dummy_head.next = head
        for _ in range(m - 1):
            cursor = cursor.next
        
        keeper = cursor
        pre = cursor.next
        cursor = pre.next
        
        for _ in range(n - m):
            post = cursor.next
            cursor.next = pre
            pre = cursor
            cursor = post
        
        keeper.next.next = cursor
        keeper.next = pre
        
        return dummy_head.next
