#!/usr/bin/env python
# encoding: utf-8
"""
path_sum_ii.py

Created by  on 2014-07-02.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/path-sum-ii/
# tags: easy, tree, dfs, sum

"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        
        res = []
        stack = []
        def check_sum(node, sub_sum):
            if node is None:
                return
            
            stack.append(node.val)
            sub_sum -= node.val
            if node.left is None and node.right is None:
                if sub_sum == 0:
                    # note: make a copy of current stack
                    res.append(list(stack))
            else:
                check_sum(node.left, sub_sum)
                check_sum(node.right, sub_sum)
            stack.pop()
        
        check_sum(root, sum)
        return res

