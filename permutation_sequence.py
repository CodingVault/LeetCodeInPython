#!/usr/bin/env python
# encoding: utf-8
"""
permutation_sequence.py

Created by Shengwei on 2014-07-15.
"""

# https://oj.leetcode.com/problems/permutation-sequence/
# tags: medium / hard, permutation, numbers, logic

"""
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
"""

fac_cache = {0: 1, 1: 1}
def fac(n):
    cached_fac = fac_cache.get(n)
    if cached_fac:
        return cached_fac
    res = n * fac(n - 1)
    fac_cache[n] = res
    return res

def get_perm(nums, k):
    # for the first k number of elements, their first a few
    # characters don't change but only a consecutive sequence
    # such as, '1234xxxx'

    # actually start the loop from the right most end,
    # the index in nums should be -i
    for i in xrange(1, len(nums) + 1):
        if fac(i) < k:
            continue
        # at this point, fac(i) >= k so the kth element
        # can be composed by the last i number of elements
        # i.e., nums[-i:]
        
        # how many (i-1)! in k, which indicates which should be
        # the first char in the permutation of nums[-i:]
        m = (k - 1) / fac(i - 1)
        
        # nth element to pick in the next iteration
        n = k % fac(i - 1)

        prefix = ''.join(map(str, nums[:-i]))
        middle = nums[-i + m]
        rest = nums[-i:]
        rest.remove(middle)

        if n == 0:
            # k == (m+1)*(i-1)!, the last element composed of
            # nums[-i:], which is reversed consecutive sequence
            # note: the edge case is i*(i-1)! which is the last
            # element of all permutation of `nums`
            rest = ''.join(map(str, reversed(rest)))
        else:
            rest = get_perm(rest, n)
        return prefix + str(middle) + rest
    
    # k > (len(nums))!
    return ''

class Solution:
    # @return a string
    def getPermutation(self, n, k):
        return get_perm(range(1, n + 1), k)
