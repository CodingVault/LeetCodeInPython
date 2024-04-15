#!/usr/bin/env python
# encoding: utf-8
"""
generate_parentheses.py

Created by Shengwei on 2014-07-28.
"""

# https://oj.leetcode.com/problems/generate-parentheses/
# tags: medium, generator, parentheses, dfs, recursion, dp

"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
"""

# CC 9.6
# DP: https://leetcode.com/problems/generate-parentheses/solutions/10369/clean-python-dp-solution/


# 20240330
def generate(count):
    res = set()
    def routine(s, left, right):
        if right == 0:
            res.add(s.decode())
            return
        if left > 0:
            routine(s + b'(', left - 1, right)
        if right > left:
            routine(s + b')', left, right - 1)
    routine(bytearray('', 'utf-8'), count, count)
    return res


# 20231104
def generate(count):
    res = []
    def routine(holder, left, right):
        if right == count:
            res.append(holder.decode())
        if left < count:
            routine(holder + b'(', left + 1, right)
        if left > right:
            routine(holder + b')', left, right + 1)
    routine(bytearray('', 'utf-8'), 0, 0)
    return res


# generator: https://leetcode.com/problems/generate-parentheses/solutions/10096/4-7-lines-python/
class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        
        def generator(s, left, right):
            if left == 0 and right == 0:
                yield s
            
            if left > 0:
                for each in generator(s + '(', left - 1, right):
                    yield each
            
            if right > left:
                for each in generator(s + ')', left, right - 1):
                    yield each
        
        return list(generator('', n, n))


# 04/14/2022 --> faster
def gen_parantheses(n):

    res = set()

    def gen(holder, left, right):
        if (right == n):
            res.add(''.join(holder))
            return

        if (left < n):
            holder.append('(')
            gen(holder, left + 1, right)
            holder.pop()

        if (right < left):
            holder.append(')')
            gen(holder, left, right + 1)
            holder.pop()

    gen([], 0, 0)

    return res


"""
In [62]: timeit(generateParenthesis(10))
35.8 ms ± 147 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

In [63]: timeit(gen_parantheses(10))
23.7 ms ± 89.8 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
"""
