#!/usr/bin/env python
# encoding: utf-8
"""
gas_station.py

Created by  on 2014-07-29.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/gas-station/
# tags: hard, logic, brain teaser

"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
"""

# https://oj.leetcode.com/discuss/1722/spoiler-alert-java-gas-station-solution-what-you-guys-think
# https://oj.leetcode.com/discuss/4159/share-some-of-my-ideas
# http://blog.shengwei.li/leetcode-gas-station/

# It can be viewed as an array consisting of (gas[i] - cost[i]), and in the array find a starting
# point from which the sum of the following rotating sequence is never negative.

class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        
        start = gap = tank = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            tank += g - c
            if tank < 0:
                start = i + 1
                gap += tank
                tank = 0
        # remember to include the last tank
        gap += tank
        
        if gap < 0:
            # there is not engough gas in total
            return -1
        return start
        # return -1 if gap < 0 else start
