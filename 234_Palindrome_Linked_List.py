#!/usr/bin/env python
# encoding: utf-8
"""
234. Palindrome Linked List

Created by Shengwei on 2023-10-06.

Used:
* Meta: https://www.1point3acres.com/bbs/thread-1026007-1-1.html
"""

# https://leetcode.com/problems/palindrome-linked-list/description/
# tags: easy / medium, linked-list, palindrome, reverse

"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?
"""

# https://leetcode.com/problems/palindrome-linked-list/solutions/64500/11-lines-12-with-restore-o-n-time-o-1-space/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """Use slow/fast cursors to reverse the first half of the list,
            and then compare pairs of nodes from the middle
        """
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        
        # length of list is odd
        if fast:
            slow = slow.next
        
        while rev and rev.val == slow.val:
            rev = rev.next
            slow = slow.next
        return not rev