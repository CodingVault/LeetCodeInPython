#!/usr/bin/env python
# encoding: utf-8
"""
linked_list_random_pointer.py

Created by  on 2014-07-01.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/copy-list-with-random-pointer/

# Better way to do it:
# https://oj.leetcode.com/discuss/753/is-there-any-faster-method?show=2962#a2962
# 1. the first loop inserts newly copied node into the original linked list
#   right after the node being copied. E.g., originally (node 0) -> (node 1) -> ...;
#   after the loop, it becomes (node 0) -> (node 0 copy) -> (node 1) -> (node 1 copy) -> ...
# 2. after the first loop, we know random pointers (p^) for the copied nodes (n^)
#   should point to the immediate following nodes of those (p) being pointed by
#   the nodes being copied (n). take the example above, if the random pointer of
#   (node 0) points at (node 1), then the random pointer of (node 0 copy) points at
#   the immediate following node of (node 1), namely (node 1 copy). this is
#   what the second loop does
# 3. collect copied nodes and reset the original list back

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
        mappings = {}  # store mappings from the label to the node
        
        # go through the list to copy normal links
        while cursor:
            copy_cursor.next = RandomListNode(cursor.label)
            
            # note: more than one nodes can have random pointers to
            #   the same node; setting the mapping value to None
            #   without checking if the label has existed will result
            #   in unwanted overwrite
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
            # mapping list during first tranversal
            if mappings.get(copy_cursor.label, 1) is None:
                mappings[copy_cursor.label] = copy_cursor
            
            if cursor.random:
                copy_cursor.random = mappings[cursor.random.label]
            
            cursor = cursor.next
            copy_cursor = copy_cursor.next
        
        return dummy_head.next

