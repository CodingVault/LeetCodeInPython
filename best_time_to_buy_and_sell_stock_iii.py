#!/usr/bin/env python
# encoding: utf-8
"""
best_time_to_buy_and_sell_stock_iii.py

Created by Shengwei on 2014-07-22.
"""

# https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
# tags: hard, array, logic, tricky, edge cases

"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

"""
TODO: to be proven (by code):

Transition from (one transaction) to (as many as possible transactions):
1. get one transaction with max profit;
2. for two transactions, they are
    a) either the prior big one transaction, and another second-max profit transaction;
    b) or the two max profit transactions broken down from the first max profit transaction;
3. for tree transactions, ...
"""

# https://oj.leetcode.com/discuss/1381/any-solutions-better-than-o-n-2
#   see also the paper: Maximum-Scoring Segment Sets

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        
        # the max profit of one trasaction from 0 up to i
        history = [0] * len(prices)
        # the max profit of one trasaction from n-1 down to i
        future = [0] * len(prices)
        
        lowest = prices[0]
        for index in xrange(1, len(prices)):
            lowest = min(lowest, prices[index])
            history[index] = max(
                history[index - 1], prices[index] - lowest)
        
        # note: there exist four possible scenarios where
        #   there is only one transaction:
        #       a) buy at 0, sell at n-1
        #       b) buy at 1, sell at n-1
        #       c) buy at 0, sell at n-2
        #       d) buy at 1, sell at n-2
        #   they are all covered by history[-1]
        max_profit = history[-1]
        
        highest = prices[-1]
        for index in xrange(-2, -len(prices), -1):
            highest = max(highest, prices[index])
            future[index] = max(
                future[index + 1], highest - prices[index])
            
            # compute max profit by splitting the prices
            # into two parts: [0, index] and (index, n-1)
            cur_profit = history[index] + future[index + 1]
            max_profit = max(max_profit, cur_profit)
        
        return max_profit
