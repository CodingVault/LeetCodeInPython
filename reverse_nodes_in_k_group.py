#!/usr/bin/env python
# encoding: utf-8
"""
reverse_nodes_in_k_group.py

Created by Shengwei on 2014-07-26.
"""

# https://oj.leetcode.com/problems/reverse-nodes-in-k-group/
# tags: medium, linked-list, pointer, dummy head, edge cases, reverse

"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""

# https://oj.leetcode.com/discuss/6113/my-solution-accepted-in-java
# alternative: reverse every two nodes at a time up to k nodes in each outer loop

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        pre = dummy_head = ListNode(0)
        dummy_head.next = head
        
        while pre.next:
            post = pre.next
            # move post to the next k+1 node or
            # None if there are just k nodes
            for _ in xrange(k):
                if post:
                    post = post.next
                else:
                    return dummy_head.next
            
            # reverse the section between pre and post
            pre_cursor = pre.next
            cursor = pre_cursor.next
            while cursor != post:
                post_cursor = cursor.next
                cursor.next = pre_cursor
                pre_cursor = cursor
                cursor = post_cursor
            
            # reconnect the head and tail of just
            # reverted section and reset pre
            pre.next.next = post
            pre.next, pre = pre_cursor, pre.next
        
        return dummy_head.next
