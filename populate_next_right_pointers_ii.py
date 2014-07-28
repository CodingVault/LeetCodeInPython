#!/usr/bin/env python
# encoding: utf-8
"""
populate_next_right_pointers_ii.py

Created by  on 2014-07-03.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
# tags: medium / hard, tree, pointer

"""
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
"""

# https://oj.leetcode.com/discuss/3339/o-1-space-o-n-complexity-iterative-solution

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        # the cursor moving around and is the parent of
        # nodes that are being connected; one level above pre and head
        cur = root
        
        # the cursor pointing at the node which is supposed
        # to be connected with the next node
        pre = None
        
        # the first node of each level - on the same level of pre;
        # it is None if pre is None
        head = None

        while cur:
            
            # process each line
            while cur:
                if cur.left:
                    if pre:
                        pre.next = cur.left
                    else:
                        # head must be None if pre is still None
                        head = cur.left
                    # pre needs to be set as cur
                    # no matter it was None or not
                    pre = cur.left
                
                if cur.right:
                    if pre:
                        pre.next = cur.right
                    else:
                        head = cur.right
                    pre = cur.right
                
                # move cursor to the next node to the right
                cur = cur.next
            
            # move cursor to the first node of the next level
            cur = head
            # reset pre and head
            pre = head = None
