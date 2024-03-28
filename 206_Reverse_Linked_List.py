#!/usr/bin/env python
# encoding: utf-8
"""
206. Reverse Linked List

Created by Shengwei on 2023-10-06.
"""

# https://leetcode.com/problems/reverse-linked-list/description/
# tags: easy / medium, linked-list, reverse

"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 20231106
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev, cur = None, head
        while cur:
            # same: rev, cur.next, cur = cur, rev, cur.next
            rev, rev.next, cur = cur, rev, cur.next
        return rev


# 20181008
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        pre, node = None, head
        while node:
            post = node.next
            node.next = pre
            pre, node = node, post
        
        return pre
