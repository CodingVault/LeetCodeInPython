#!/usr/bin/env python
# encoding: utf-8
"""
minimal_window_string.py

Created by Shengwei on 2014-07-06.
"""

# https://oj.leetcode.com/problems/minimum-window-substring/
# tags: hard, string, hashtable, minimal, edge cases, clarification (dups)

"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the emtpy string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
"""

# https://leetcode.com/problems/minimum-window-substring/discuss/26804/12-lines-Python


# 20240412
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """Valid example:
            s -> 'ABBDCA', t -> 'ABC'
        """
        if len(s) < len(t):
            return ''

        from collections import Counter
        counter = Counter(t)
        size = len(t)
        
        # use `end` as a flag; it will be a valid index if moved
        begin, end = 0, len(s)  # define current min window
        left = right = 0  # define sliding window

        while right < len(s):
            if s[right] in counter:
                counter[s[right]] -= 1
                if counter[s[right]] >= 0:
                    size -= 1
            
            while size == 0:
                if s[left] in counter:
                    counter[s[left]] += 1
                    if counter[s[left]] > 0:
                        size += 1
                        if end - begin > right - left:
                            begin, end = left, right
                left += 1
            
            right += 1
        
        return s[begin:end+1] if end < len(s) else ''



"""
Notes for 3 bugs while implementing:
1. should move left pointer when substring is set other than left > 0;
    alternatively, set left to -1 in the beginning and later check if it's > -1
2. should check counter == char_count only when counter just changed
3. should decrease counter only when lookup_dict entry is -1, which means
    it just dissatisfies the minimum requirements

The last two are mainly due to the change of concept -- there can be dups in T.
"""

# TODO:
#   1. refactor it using a queue
#   2. do not need to store both index and the char

class Solution:
    # @return a string
    def minWindow(self, S, T):
        """Think about a windown sliding through S."""
        window, counter, char_count = [], 0, len(set(T))
        left = right = 0
        min_substring = ''
    
        # initialize lookup dictionary, with negative count of
        # each char in T; they are expected to be supplimented
        # by sliding the window on S
        lookup_dict = collections.defaultdict(int)
        for char in T:
            lookup_dict[char] -= 1
    
        while right < len(S):
        
            if window and left > window[0][1]:
                # drop off the left most one from the window;
                # the count of such item in the window decreases
                to_be_removed = window.pop(0)[0]
                lookup_dict[to_be_removed] -= 1
            
                # IMPORTANT! should check if it's -1 other than < 0
                if lookup_dict[to_be_removed] == -1:
                    # no such char is in the window now, decrease count
                    counter -= 1
        
            if S[right] in lookup_dict:
                # include S[right] in the window
                window.append((S[right], right))
                lookup_dict[S[right]] += 1
            
                if lookup_dict[S[right]] == 0:
                    # requirement for S[right] has been just satisfied;
                    # if there were more than enough S[right], no change
                    counter += 1
                
                    # only check this when counter increases
                    if counter == char_count:
                        # all requirements for T have been satisfied;
                        # shrink the window for mimimum substring
                    
                        while lookup_dict[window[0][0]] > 0:
                            # the left most item in the window is
                            # superfluous, drop it
                            lookup_dict[window.pop(0)[0]] -= 1
                    
                        # shrink the window to the tighter boundary
                        left = window[0][1]
                    
                        # update minimum substring; after all chars in T have
                        # been in the window, the window only shrinks or
                        # at least has no change, so do not need comparison
                        min_substring = S[left:right+1]
        
            # slide the window to the right
            right += 1
            # move the left of the window after we've found a substring
            if min_substring:
                left += 1
    
        return min_substring
