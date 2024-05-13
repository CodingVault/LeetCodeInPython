#!/usr/bin/env python
# encoding: utf-8
"""
274. H-Index

Created by Shengwei on 2025-05-10.

Used:
- TikTok: https://www.1point3acres.com/bbs/thread-1065902-1-1.html
"""

# https://leetcode.com/problems/h-index/description/
# tags: medium / hard, logic, array, tricky

"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

 

Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
Example 2:

Input: citations = [1,3,1]
Output: 1
 

Constraints:

n == citations.length
1 <= n <= 5000
0 <= citations[i] <= 1000
"""

# https://leetcode.com/problems/h-index/solutions/71055/1-line-python-solution/
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        return sum(i < j for i, j in enumerate(sorted(citations, reverse=True)))


# from faster solutions
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = len(citations)
        for i in sorted(citations):
            if i >= h:
                return h
            h -= 1
