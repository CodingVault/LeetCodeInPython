#!/usr/bin/env python
# encoding: utf-8
"""
restore_ip_address.py

Created by Shengwei on 2014-07-04.
"""

# https://oj.leetcode.com/problems/restore-ip-addresses/

"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""

# https://oj.leetcode.com/discuss/77/restore-ip-addresses
# tags: medium, string, dp, generator, dfs

# TODO: DP or 3 loops
# put 3 dots in len(s) - 1 places, but the distance between two dots must be 1 - 3,
# so it's must be less than 3 * 3 * 3 choices in total


########## V2 ##########

def valid_sec(string):
    """Check if string is a valid IP address section"""
    if len(string) == 0:
        return False
    num = int(string)
    if string != str(num):
        # invalid string like "000" -- only one "0" is okay
        return False
    return num >= 0 and num <= 255

class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        
        def restore(substring, sec_count):
            if sec_count == 1:
                if valid_sec(substring):
                    yield substring
                return
            
            for i in range(1, 4):
                cur_sec = substring[:i]
                if valid_sec(cur_sec):
                    remainder = substring[i:]
                    for each in restore(remainder, sec_count - 1):
                        yield cur_sec + "." + each
        
        return list(restore(s, 4))


########## V1 ##########
# it doesn't need to have the loop: for left_sec in xrange(1, sec_num);
# doing it in DP only needs to break it into 1 + 3

class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        if s is None:
            return []
        
        def valid_sec(string):
            """Check if string is a valid IP address section"""
            num = int(string)
            if string != str(num):
                return False
            if num >= 0 and num <= 255:
                return True
            return False
        
        cache = collections.defaultdict(dict)
        def form_addr(string, sec_num):
            if len(string) < 1 * sec_num or len(string) > 3 * sec_num:
                return set()
            
            if sec_num in cache[string]:
                return cache[string][sec_num]
            
            if sec_num == 1 and valid_sec(string):
                res = set([string])
            else:
                res = set()
            
            for left_sec in xrange(1, sec_num):
                for i in xrange(1, len(string)):
                    left = form_addr(string[:i], left_sec)
                    right = form_addr(string[i:], sec_num - left_sec)
                    if left and right:
                        for one_left in left:
                            for one_right in right:
                                res.add(one_left + '.' + one_right)
            
            cache[string][sec_num] = res
            return res
            
        return list(form_addr(s, 4))
