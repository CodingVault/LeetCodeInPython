#!/usr/bin/env python
# encoding: utf-8
"""
best_time_to_buy_and_sell_stocks.py

Created by  on 2014-07-15.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock/

"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
"""

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if prices is None or len(prices) == 0:
            return 0

        max_profit = 0
        lowest = prices[0]
        highest = prices[0]
        
        for price in prices:
            if price > highest:
                highest = price
            if price < lowest:
                max_profit = max(highest - lowest, max_profit)
                lowest = price
                highest = price
        
        # remember to check the difference of the pair
        # of highest and lowest in the end
        return max(highest - lowest, max_profit)