#!/usr/bin/env python
# encoding: utf-8
"""
rotate_list.py

Created by Shengwei on 2014-07-15.
"""

# https://oj.leetcode.com/problems/rotate-list/
# tags: easy / medium, linked-list, rotate, edge cases, clarification

"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""

# note: k may be larger than the length of list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

############## O(n) ##############
class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head is None:
            return None
        
        follower = front = head
        for _ in xrange(k):
            if front.next:
                front = front.next
            else:
                front = head
        
        if front == head:
            # k % len(list) == 0
            return head
        
        while front.next:
            front = front.next
            follower = follower.next
        
        front.next = head
        head = follower.next
        follower.next = None
        
        return head

############## O(kn) ##############
class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head is None or head.next is None:
            return head

        for _ in xrange(k):
            before_tail = head
            while before_tail.next.next is not None:
                before_tail = before_tail.next

            before_tail.next.next = head
            head = before_tail.next
            before_tail.next = None
        
        return head
