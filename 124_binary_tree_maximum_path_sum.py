#!/usr/bin/env python
# encoding: utf-8
"""
binary_tree_maximum_path_sum.py

Created by Shengwei on 2014-07-20.
"""

# https://oj.leetcode.com/problems/binary-tree-maximum-path-sum/
# tags: medium / hard, tree, recursion, sum, dfs

"""
Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
"""

# https://oj.leetcode.com/discuss/6253/whats-wrong-with-binary-tree-maximum-path-sum-solution-python

# TODO: try D&C

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 20240330
class Solution:

    def __init__(self):
        self.cur_max = 0

    def max_sum(self, node):
        if not node:
            return 0

        # print('current', node.value)
        left_sum = self.max_sum(node.left)
        # print('left', left_sum)
        right_sum = self.max_sum(node.right)
        # print('right', right_sum)
        self.cur_max = max(cur_max, left_sum + right_sum + node.value)
        # print('cur_max', self.cur_max)
        return max(0, left_sum + node.value, right_sum + node.value)

    def maxPathSum(self, root):
        self.max_sum(root)
        return self.cur_max


# 2014
class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        
        def max_sum(node):
            """Returns a tuple:
                1. maximum value of
                    a. the max path sum including current node
                    b. the max path sum of left subtree
                    c. the max path sum of right subtree
                2. max upward sum, up to current node
            """
            
            if node is None:
                return (-100000000, 0)
            
            max_left, left_sum = max_sum(node.left)
            max_right, right_sum = max_sum(node.right)
            
            # sum of path: left child path, right child path and
            # current node, where left child path and right child
            # path only contribute positive sub-sum
            passing_through = left_sum + node.val + right_sum
            
            max_child_sum = max(left_sum, right_sum)
            
            return (max(passing_through, max_left, max_right),
                    max(max_child_sum + node.val, 0))
        
        return max_sum(root)[0]


# sum_down is unnecessary
class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        
        def max_sum(node, sum_down):
            """Returns a tuple:
                1. maximum value of
                    a. the max path sum including current node
                    b. the max path sum of left subtree
                    c. the max path sum of right subtree
                2. max upward sum, up to current node
                
            Note:
                1. assume sum_down >= 0
                2. return upward sum >= 0
            """
            
            if node is None:
                return (-100000000, 0)
            
            # note: don't use this to compute max_path_sum in case
            #   node.val is negative -- max_path_sum might be negative
            cur_down = max(sum_down + node.val, 0)
            max_left, left_sum = max_sum(node.left, cur_down)
            max_right, right_sum = max_sum(node.right, cur_down)
            
            max_child_sum = max(left_sum, right_sum)
            
            # the max path sum including current node
            max_path_sum = max(
                # downward sum + current node + max upward sum
                sum_down + node.val + max_child_sum,
                # left upward sum + current node + right upward sum
                left_sum + node.val + right_sum
            )
            
            return (max(max_path_sum, max_left, max_right),
                    max(max_child_sum + node.val, 0))
        
        return max_sum(root, 0)[0]
