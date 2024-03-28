#!/usr/bin/env python
# encoding: utf-8
"""
528. Random Pick with Weight

Created by Shengwei on 2023-11-05.

Used:
* Meta: https://www.1point3acres.com/bbs/thread-1026011-1-1.html
"""

# https://leetcode.com/problems/random-pick-with-weight/description/
# tags: medium, array, random, probability, binary

"""
You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).
 

Example 1:

Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]

Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.
Example 2:

Input
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output
[null,1,1,1,1,0]

Explanation
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It is returning the second element (index = 1) that has a probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It is returning the first element (index = 0) that has a probability of 1/4.

Since this is a randomization problem, multiple answers are allowed.
All of the following outputs can be considered correct:
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
and so on.
 

Constraints:

1 <= w.length <= 104
1 <= w[i] <= 105
pickIndex will be called at most 104 times.
"""


# 20231105

#Inspired by https://leetcode.com/problems/random-pick-with-weight/solutions/154044/java-accumulated-freq-sum-binary-search/
class Solution:

    def __init__(self, w: List[int]):
        self.slots = w.copy()
        for index in range(1, len(w)):
            self.slots[index] += self.slots[index - 1]

    def pickIndex(self) -> int:
        import random
        pick = random.randrange(self.slots[-1]) + 1
        left, right = 0, len(self.slots) - 1
        while left < right:
            mid = (left + right) // 2
            mid_slot = self.slots[mid]
            if mid_slot == pick:
                return mid
            if mid_slot < pick:
                left = mid + 1
            else:
                right = mid
        
        return left


# Memory Limit Exceeded
class Solution:

    def __init__(self, w: List[int]):
        self.array = []
        for i, wi in enumerate(w):
            self.array += [i] * wi
        self.size = len(self.array)

    def pickIndex(self) -> int:
        import random
        return self.array[random.randrange(self.size)]


# 20220430
class Solution:

    def __init__(self, w: List[int]):
        self.slots = [0]
        for num in w:
            self.slots.append(self.slots[-1] + num)
        # print(self.slots)

    def pickIndex(self) -> int:
        import random
        pick = random.randrange(self.slots[-1]) + 1
        # print(pick)
        pos = self._search(pick)
        return pos
        
    def _search(self, pick: int) -> int:
        left, right = 0, len(self.slots)
        while left < right:
            mid = (left + right) // 2
            mid_slot = self.slots[mid]
            if mid_slot == pick:
                return mid
            
            if mid_slot > pick:
                right = mid
            else:
                left = mid + 1
        
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
