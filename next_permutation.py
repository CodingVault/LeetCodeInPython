#!/usr/bin/env python
# encoding: utf-8
"""
next_permutation.py

Created by  on 2014-07-08.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/next-permutation/

"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

# 1. search from right to left and stop at first number num(i) that is less than num(i+1)
# 2. switch num(i) with the least greater number in num[i:-1]
# 3. reverse all the numbers in num[i:-1]