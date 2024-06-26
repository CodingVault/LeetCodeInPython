#!/usr/bin/env python
# encoding: utf-8
"""
binary_tree_inorder.py

Created by Shengwei on 2014-07-04.
"""

# https://oj.leetcode.com/problems/binary-tree-inorder-traversal/
# tags: easy, tree, traversal, dfs

"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?

confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
"""

# http://leetcode.com/2010/04/binary-search-tree-in-order-traversal.html (404)

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 20231029
def inorder(root):
    """logic:
    1. put node to stack when it's not None and move to the left
        - this cannot be: put node's left to the stack when its not None;
            it will remove the left child and then put it back when visiting its parent later
        - alternative: add the left child regardless of its None or not;
            see the next solution below for adaption to that approach
    2. process the top of stack if it has no left, then put the right in stack
    """
    cur = root
    stack = []
    while stack or cur:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            node = stack.pop()
            print(node.value)
            cur = node.right



class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        res = []
        stack = [root]
        
        # process stack if it has at least one
        # element that is not None
        while len(stack) > 1 or stack[-1]:
            # if the top element in the stack is None,
            # it means left subtree has been processed;
            # in other words, the second top element
            # should be processed now.
            
            # if it's not None, add left subtree to stack
            if stack[-1]:
                stack.append(stack[-1].left)
            else:
                # pop up the None element
                # alternative: stack[-2:] = [stack[-2].right]
                stack.pop()
                
                node = stack.pop()
                res.append(node.val)
                stack.append(node.right)
        
        return res
