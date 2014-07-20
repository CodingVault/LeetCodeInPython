#!/usr/bin/env python
# encoding: utf-8
"""
set_matrix_zeros.py

Created by  on 2014-07-06.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/set-matrix-zeroes/

"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

# https://oj.leetcode.com/discuss/1650/is-there-a-better-constant-space-solution

# Note:
#  1. it's possible to use only one variable to mark if there is 0 in the first column
#  2. there are two ways to set 0's:
#    a) go through markers and mark entire rows or columns
#    b) go through the matrix and see if it's on row or column of any marker