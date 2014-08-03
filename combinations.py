#!/usr/bin/env python
# encoding: utf-8
"""
combinations.py

Created by Shengwei on 2014-07-06.
"""

# https://oj.leetcode.com/problems/combinations/
# tags: medium, combination, recursion, dp, dfs

"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

# TODO: use explicit dp matrix instead of recursion
"""
pseudo-code
  for j in [1..n]:
    matrix[1][j] = [[j]]
    
  for i in [2..k]:  # length of each combination
    for j in [i..n]:  # current number
      for k in [i-1 .. j-1]:  # loop through prior combinations for number < j
        matrix[i][j] = []
        for each in matrix[i-1][k]:
          each.append(j)
          matrix[i][j].append(each)
  
  result = []
  # collect all combinations for sub_combinations from matrix[k][k..n]
  for j in [k..n]:
    result.extend(matrix[k][j])
"""

# TODO: dfs

class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        
        def comb(array, k):
            if array is None or k > len(array):
                return []
            if k == 0:
                return [[]]
            
            # k >= 1, so len(array) >= k >= 1
            one = array.pop()
            
            # note: use copy.copy here!
            res = comb(copy.copy(array), k)
            for sub_comb in comb(copy.copy(array), k - 1):
                res.append(sub_comb + [one])
            
            return res
        
        return comb(range(1, n+1), k)
