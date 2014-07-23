#!/usr/bin/env python
# encoding: utf-8
"""
candy.py

Created by  on 2014-07-22.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/candy/
# tags: hard, array, greedy, logic

"""
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
"""

# https://oj.leetcode.com/discuss/76/does-anyone-have-a-better-idea
# TODO: try alternative

class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        count = [1]
        
        for index in xrange(1, len(ratings)):
            # note: child gets the same rating can have fewer
            # candies than the neighbors
            # e.g., rating [1, 2, 2, 3] -> candies [1, 2, 1, 2]
            if ratings[index] > ratings[index-1]:
                count.append(count[-1] + 1)
            else:
                count.append(1)
        
        for index in xrange(-2, -len(ratings)-1, -1):
            if ratings[index] > ratings[index+1]:
                count[index] = max(count[index], count[index+1] + 1)
        
        return sum(count)