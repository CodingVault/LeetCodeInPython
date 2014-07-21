#!/usr/bin/env python
# encoding: utf-8
"""
copy_list_with_random_pointer.py

Created by  on 2014-07-15.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/copy-list-with-random-pointer/

"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""

# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head is None:
            return head
        
        # init a dummy head
        copy_cursor = dummy_head = RandomListNode(0)
        cursor = head
        mappings = {}
        
        # go through the list to copy normal links
        while cursor:
            copy_cursor.next = RandomListNode(cursor.label)
            
            if cursor.random and cursor.random.label not in mappings:
                mappings[cursor.random.label] = None
            # store the mapping for previous node linking to this
            if copy_cursor.next.label in mappings:
                mappings[copy_cursor.next.label] = copy_cursor.next
            
            cursor = cursor.next
            copy_cursor = copy_cursor.next
        
        cursor, copy_cursor = head, dummy_head.next
        while cursor:
            # populate the mapping for node after this but having
            # a random link to this node; label was put in the
            # mapping during first tranversal
            if mappings.get(copy_cursor.label, 1) is None:
                mappings[copy_cursor.label] = copy_cursor
            
            if cursor.random:
                copy_cursor.random = mappings[cursor.random.label]
            
            cursor = cursor.next
            copy_cursor = copy_cursor.next
        
        return dummy_head.next