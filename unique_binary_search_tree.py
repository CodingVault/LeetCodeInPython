#!/usr/bin/env python
# encoding: utf-8
"""
unique_binary_search_tree.py

Created by Shengwei on 2014-07-04.
"""

# https://oj.leetcode.com/problems/unique-binary-search-trees/
# medium, tree, bst, recursion, dp

"""
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

# choose a number as the root and recursively build subtrees with
# left and right subarrays. there are n numbers to pick as the root.
# F(n) = F(0)*F(n-1) + F(1)*F(n-2) + F(2)*F(n-3) + ... + F(n-1)*F(0)
# F(0) = F(1) = 1

class Solution:
    # @return an integer
    def numTrees(self, n):
        if n == 0:
            return 0

        counts = [1, 1]
        for i in xrange(2, n + 1):
            # IMPORTANT! adding one element by `append`;
            # not counts[i] = 0
            counts.append(0)
            for j in xrange(i):
                counts[i] += counts[j] * counts[i - 1 - j]
        
        return counts[n]
