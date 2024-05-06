#!/usr/bin/env python
# encoding: utf-8
"""
437. Path Sum III

Created by Shengwei on 2024-04-13.
"""

# https://leetcode.com/problems/path-sum-iii/description/
# tags: medium / hard, tree, sum, dfs

"""
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

 

Example 1:


Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
 

Constraints:

The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000
"""

# https://leetcode.com/problems/path-sum-iii/solutions/141424/python-step-by-step-walk-through-easy-to-understand-two-solutions-comparison/
# TODO: use cache to reverse the search for full targetSum, putting 1 in cache ahead to pick up later




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        from functools import cache

        @cache
        def sub(node, target):
            if not node:
                return 0

            count = dfs(node, target)
            count += sub(node.left, targetSum)
            # print('left full:', node.val, count)
            count += sub(node.right, targetSum)
            # print('right full:', node.val, count)
            
            # print(node.val, target, count, list(n.val for n in processed if n))
            return count
        
        def dfs(node, target):
            """dfs search must separate from `sub` so full targetSum search only happens once
            """
            if not node:
                return 0

            count = dfs(node.left, target - node.val)
            # print('left res:', node.val, count)
            count += dfs(node.right, target - node.val)
            # print('right res:', node.val, count)
            if node.val == target:
                count += 1
            return count

        return sub(root, targetSum)
