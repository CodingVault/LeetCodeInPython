#!/usr/bin/env python
# encoding: utf-8
"""
301. Remove Invalid Parentheses

Created by Shengwei on 2022-04-21.

Used:
* Google onsite interview (myself)
"""

# https://leetcode.com/problems/remove-invalid-parentheses/
# tags: medium, string, dfs, bfs

"""
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return all the possible results. You may return the answer in any order.


Example 1:

Input: s = "()())()"
Output: ["(())()","()()()"]

Example 2:

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

Example 3:

Input: s = ")("
Output: [""]
 

Constraints:

1 <= s.length <= 25
s consists of lowercase English letters and parentheses '(' and ')'.
There will be at most 20 parentheses in s.
"""

"""another thought (20240505):

 - remove excessive ')' from left to right, and record positions where to remove them.
    this will be a list of possible solutions, where each solution is a list of indices for ')'
 - reverse the string including swap '(' and ')', and repeat the step above
 - multiple the solutions from both steps, one for excessive '(' and another for excessive ')'

this should avoid duplicate processing of reversed strings in the original solutions below.
"""



# https://leetcode.com/problems/remove-invalid-parentheses/discuss/75027/Easy-Short-Concise-and-Fast-Java-DFS-3-ms-solution

# 20190407
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        ret = []
        def remove(s_to_check, start_from, pointer, left_to_right):
            '''
            start_from: start point to check if the char is ')'; it should not be ')' to begin with
                (this prevents repeatitive checks)
            pointer: loop through the string `s`
            '''
            counter = 0
            
            while pointer < len(s_to_check):
                if s_to_check[pointer] == '(':
                    counter += 1
                elif s_to_check[pointer] == ')':
                    counter -= 1
                
                if counter >= 0:
                    pointer += 1
                    continue
                
                # pointer points to the char of excessive ')'
                i = start_from
                while i <= pointer:
                    # should check `i != start_from` instead of `i > 0`:
                    # the sequence prior to `start_from` has aligned
                    if s_to_check[i] == ')' and (i == start_from or s_to_check[i - 1] != ')'):
                        remove(s_to_check[:i] + s_to_check[i+1:], i, pointer, left_to_right)
                    
                    i += 1
                return
            
            mapping = {'(': ')', ')': '('}
            reversed_s = ''.join(mapping.get(ch, ch) for ch in reversed(s_to_check))
            if counter > 0:
                remove(reversed_s, 0, 0, False)
            else:
                # counter == 0, all excessive parentheses have been removed
                ret.append(s_to_check) if left_to_right else ret.append(reversed_s)
        
        remove(s, 0, 0, True)
        return ret


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        def check(s_to_check, start_from, pointer, left_to_right):
            counter = 0
            while pointer < len(s_to_check):
                if s_to_check[pointer] == '(':
                    counter += 1
                elif s_to_check[pointer] == ')':
                    counter -= 1
                
                if counter < 0:
                    break
                pointer += 1

            if counter >= 0:
                mapping = {'(': ')', ')': '('}
                reversed_s = ''.join(mapping.get(ch, ch) for ch in reversed(s_to_check))
                if counter > 0:
                    for to_check in check(reversed_s, 0, 0, not left_to_right):
                        yield to_check
                else:
                    # Note: add different string depending on direction of checking
                    if left_to_right: yield s_to_check
                    else: yield reversed_s

            else:
                # pointer points to the char of excessive ')'
                i = start_from
                while i <= pointer:
                    # should check `i != start_from` instead of `i > 0`:
                    # the sequence prior to `start_from` has aligned
                    if s_to_check[i] == ')' and (i == start_from or s_to_check[i - 1] != ')'):
                        for to_check in check(s_to_check[:i] + s_to_check[i+1:], i, pointer, left_to_right):
                            yield to_check
                    
                    i += 1
        
        return list(check(s, 0, 0, True))


# iterative
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        ret = []
        to_check = [(s, 0, 0, True)]

        while to_check:            
            s_to_check, start_from, pointer, left_to_right = to_check.pop()
            counter = 0
            while pointer < len(s_to_check):
                if s_to_check[pointer] == '(':
                    counter += 1
                elif s_to_check[pointer] == ')':
                    counter -= 1
                
                if counter < 0:
                    break
                pointer += 1

            if counter >= 0:
                mapping = {'(': ')', ')': '('}
                reversed_s = ''.join(mapping.get(ch, ch) for ch in reversed(s_to_check))
                if counter > 0:
                    to_check.append((reversed_s, 0, 0, not left_to_right))
                else:
                    # Note: add different string depending on direction of checking
                    ret.append(s_to_check) if left_to_right else ret.append(reversed_s)

            else:
                # pointer points to the char of excessive ')'
                i = start_from
                while i <= pointer:
                    # should check `i != start_from` instead of `i > 0`:
                    # the sequence prior to `start_from` has aligned
                    if s_to_check[i] == ')' and (i == start_from or s_to_check[i - 1] != ')'):
                        to_check.append((s_to_check[:i] + s_to_check[i+1:], i, pointer, left_to_right))
                    
                    i += 1
        
        return ret