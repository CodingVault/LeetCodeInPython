#!/usr/bin/env python
# encoding: utf-8
"""
path_sum_ii.py

Created by  on 2014-07-02.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/path-sum-ii/

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

import copy

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        
        res = []
        def check_sum(root, sub_sum, nodes):
            if root is None:
                return
            
            nodes.append(root.val)
            sub_sum -= root.val
            if root.left is None and root.right is None:
                if sub_sum == 0:
                    res.append(nodes)
            else:
                check_sum(root.left, sub_sum, copy.copy(nodes))
                check_sum(root.right, sub_sum, copy.copy(nodes))
        
        check_sum(root, sum, [])
        return res

