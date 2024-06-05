#!/usr/bin/env python
# encoding: utf-8
"""
1055. Shortest Way to Form String

Created by Shengwei on 2025-05-30.

Used:
- Pinterest: https://www.1point3acres.com/bbs/thread-1068940-1-1.html
"""

# locked
# tags: medium, string, shortest

"""
From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.

 

Example 1:

Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".

Example 2:

Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.

Example 3:

Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".
 

Constraints:

Both the source and target strings consist of only lowercase English letters from "a"-"z".
The lengths of source and target string are between 1 and 1000.

"""

def form(source, target):
    ti = 0
    res = 0
    while ti < len(target):
        si = 0
        old_ti = ti
        res += 1
        while si < len(source):
            if source[si] == target[ti]:
                ti += 1
                if ti == len(target):
                    return res
            si += 1
        if ti == old_ti:
            return -1
    return -1

# alternative
def form(source, target):
    ti = 0
    res = 0
    while ti < len(target):
        si = 0
        old_ti = ti
        res += 1
        while si < len(source) and ti < len(target):
            if source[si] == target[ti]:
                ti += 1
            si += 1
        if ti == old_ti:
            return -1
    return res
