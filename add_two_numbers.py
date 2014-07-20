#!/usr/bin/env python
# encoding: utf-8
"""
add_two_numbers.py

Created by  on 2014-07-09.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/add-two-numbers/

"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

# https://oj.leetcode.com/discuss/2308/is-this-algorithm-optimal-or-what

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        cursor = dummy_header = ListNode(0)
        carry = 0
        while l1 and l2:
            x = l1.val + l2.val + carry
            carry, remainder = x / 10, x % 10
            cursor.next = ListNode(remainder)
            
            cursor = cursor.next
            l1 = l1.next
            l2 = l2.next
        
        l = l1 if l1 else l2
        while carry and l:
            if l.val == 9:
                cursor.next = ListNode(0)
            else:
                cursor.next = ListNode(l.val + 1)
                carry = 0
            cursor = cursor.next
            l = l.next
            
        if carry:
            cursor.next = ListNode(1)
        else:
            cursor.next = l
            
        return dummy_header.next