#!/usr/bin/env python
# encoding: utf-8
"""
best_time_to_buy_and_sell_stock_ii.py

Created by Shengwei on 2014-07-22.
"""

# https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# tags: easy / medium, array, greedy, logic

"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

# https://oj.leetcode.com/discuss/2012/is-this-question-a-joke

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        
        max_profit = 0
        lowest = highest = prices[0]
        
        for price in prices:
            if price > highest:
                highest = price
            
            elif price < highest:
                # harvest the profit before price drops
                max_profit += highest - lowest
                lowest = highest = price
        
        # IMPORTANT! add the last pair of difference
        return max_profit + highest - lowest
