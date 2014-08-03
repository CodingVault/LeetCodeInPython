#!/usr/bin/env python
# encoding: utf-8
"""
binary_tree_postorder.py

Created by Shengwei on 2014-06-30.
"""

# https://oj.leetcode.com/problems/binary-tree-postorder-traversal/
# tags: medium, tree, traversal, dfs

"""
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?
"""

##### V3 #####

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if root is None:
            return []

        res = []
        stack = [root, root.left]
        
        while len(stack) > 1:
            
            if stack[-1] is not None:
                stack.append(stack[-1].left)
            
            elif stack[-2] is not None:
                stack.append(stack[-2].right)
            
            else:
                res.append(stack[-3].val)
                stack[-3:] = [None]
      
        return res


##### V2 #####
# http://leetcode.com/2010/10/binary-tree-post-order-traversal.html

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if root is None:
            return []

        res = []
        stack = [root]
        
        # denote the last visited node
        # note: this should never be None, otherwise it may confuse
        #   the processing; a node's child could be None itself, but
        #   it doesn't mean the None child has been visited
        pre = root
        
        while stack:
            
            # visit the node, if
            #   1. both children are None -- leaf node, or
            #   2. left child has been visited and there is no right child, or
            #   3. right child has been visited
            if (stack[-1].left is None and stack[-1].right is None
                    or stack[-1].left == pre and stack[-1].right is None
                    or stack[-1].right == pre):
                pre = stack.pop()
                res.append(pre.val)
            
            # put right child in the stack, if
            #   1. left child is None -- right child cannot be None because of
            #       prior if statement, or
            #   2. left child has been visited
            elif stack[-1].left is None or stack[-1].left == pre:
                stack.append(stack[-1].right)
            
            # put left child in the stack -- it cannot be None because of prior
            # if statement
            else:
                stack.append(stack[-1].left)
        
        return res


##### V1 #####

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if root is None:
            return []

        res = []
        stack = [root]
        while stack:
            node = stack[-1]
            if node.right is None and node.left is None:
                node = stack.pop()
                res.append(node.val)
                continue

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            
            # note: it's crucial to set left and right as None,
            #   otherwise this node won't be popped out
            node.left = node.right = None
        
        return res

