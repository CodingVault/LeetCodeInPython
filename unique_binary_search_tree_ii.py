#!/usr/bin/env python
# encoding: utf-8
"""
unique_binary_search_tree_ii.py

Created by  on 2014-07-08.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/unique-binary-search-trees-ii/

"""
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

# https://oj.leetcode.com/discuss/3440/help-simplify-my-code-the-second-one

"""
class Solution:
    def build(self, nodes):
        n = len(nodes)
        if n == 0:
            yield None
            return
        for i in range(n):
            root = nodes[i]
            for left in self.build(nodes[:i]):
                for right in self.build(nodes[i+1:]):
                    root.left, root.right = left, right
                    yield root

    # @return a list of tree node
    def generateTrees(self, n):
        nodes = map(TreeNode, range(1, n + 1))
        return map(copy.deepcopy, self.build(nodes))
"""