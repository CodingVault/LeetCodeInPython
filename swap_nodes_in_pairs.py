#!/usr/bin/env python
# encoding: utf-8
"""
swap_nodes_in_pairs.py

Created by  on 2014-07-08.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/swap-nodes-in-pairs/
# tags: medium, linked-list, pointers, logic, edge cases

"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

############### V2 ###############
# handle the outgoing pointer of current pair directly
class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        
        pre, post = head, head.next
        head = post
        while post != pre:
            # post is not None and post == pre.next
            
            if post.next and post.next.next:
                pre.next = post.next.next
            else:
                # there is one following node or none
                pre.next = post.next
            
            post.next, pre = pre, post.next
            
            # post could be pre if there is one
            # following node or none
            post = post.next.next
        
        return head

############### V1 ###############
# use a temp variable holding the outgoing pointer
# of prior pair of nodes, and update it later
class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        
        pre, post = head, head.next
        keeper = dummy_head = ListNode(0)
        while post:
            pre.next = post.next
            post.next = pre
            
            keeper.next = post
            keeper = pre
            
            pre = keeper.next
            post = pre.next if pre else None
        
        return dummy_head.next