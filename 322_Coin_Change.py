#!/usr/bin/env python
# encoding: utf-8
"""
322. Coin Change

Created by Shengwei on 2025-06-04.

Used:
- Disney: https://www.1point3acres.com/bbs/thread-667201-1-1.html
"""

# https://leetcode.com/problems/coin-change/description/
# tags: medium, array, dp, bfs

"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 
Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""

# 20240605 - bottom-up dp
class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        """gradually increase amount `i` and find the count for it in cache;
        the count for the current `i` (and all to the left) would be already the minimum

        add possible coins to the amount `i` and update the count for the new amount
        (on the right of amount `i` in cache) if necessary
        """
        if amount == 0: return 0
        if amount in coins: return 1

        cache = {c: 1 for c in coins}
        for i in range(min(coins), amount):
            count = cache.get(i)
            if not count:
                continue

            for c in coins:
                next_amount = i + c
                current = cache.get(next_amount, count + 1)
                cache[next_amount] = min(current, count + 1)
        
        return cache.get(amount, -1)

# alternative
class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        if amount in coins: return 1

        cache = {c: 1 for c in coins}
        for i in range(min(coins) + 1, amount + 1):
            for c in coins:
                if i - c not in cache:
                    continue
                possible_count = cache[i - c] + 1
                current = cache.get(i, possible_count)
                cache[i] = min(current, possible_count)
        
        return cache.get(amount, -1)


# 20240604 - top-down dp
class Solution:

    def __init__(self):
        self.cache = {}

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount in self.cache:
            return self.cache[amount]
        
        if amount == 0:
            return 0

        if amount < min(coins):
            return -1

        min_count = float('inf')
        for c in coins:
            sub = self.coinChange(coins, amount - c) + 1
            if 0 < sub < min_count:
                min_count = sub
        
        if min_count == float('inf'):
            min_count = -1
        self.cache[amount] = min_count
        return min_count

# alternative - use @cache
class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def check(total):
            if total == 0:
                return 0

            if total < min(coins):
                return -1

            min_count = float('inf')
            for c in coins:
                sub = check(total - c) + 1
                if 0 < sub < min_count:
                    min_count = sub
            
            return -1 if min_count == float('inf') else min_count
        
        return check(amount)


# 20181014 - bfs
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins: return -1
        if not amount: return 0

        coins.sort()
        count = 0
        cache = set([amount])
        stack = [amount]
        while stack:
            holder = []
            count += 1
            for total in stack:
                for coin in coins:
                    if coin > total:
                        break
                    
                    if coin == total:
                        return count
                    
                    rest = total - coin
                    if rest not in cache:
                        cache.add(rest)
                        holder.append(rest)
            
            stack = holder
        return -1
