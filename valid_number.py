#!/usr/bin/env python
# encoding: utf-8
"""
valid_number.py

Created by  on 2014-08-01.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/valid-number/
# tags: medium, numbers, clarification, logic, edge cases

"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.
"""

# https://oj.leetcode.com/discuss/5358/share-my-ac-code

# TODO: try regex

class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        """Overall, consider 4 situations for each char:
            1. be the first char
            2. be the last char
            3. be the single char
            4. duplicate
        """
        
        s_heading_space = True
        s_trailing_space = False
        
        # control that there is only one sign for the
        # number or exponent
        s_signed = False
        
        # make sure 'e' is not the last char;
        # alternative: these are in fact mutually exclusive,
        #   plus with s_integer and s_decimal
        s_exponent_pending = False
        s_exponent = False
        
        s_integer = False
        
        # 1. '.' followed by an integer
        # 2. an integer followed by '.'
        s_decimal = False
        
        # meet '.' before any integer, i.e., single '.';
        # alternative: mutually exclusive with s_integer
        #   and s_decimal, consider s_integer = 1,
        #   s_dot = 2, s_decimal = 3
        s_dot = False
        
        for c in s:
            if c == ' ':
                if not s_heading_space:
                    s_trailing_space = True
            
            elif c in ('+', '-'):
                # sign may appear once separately
                # for the number and exponent;
                # exponent reset s_signed to False
                if s_signed:
                    return False
                s_signed = True
                
                s_heading_space = False
                if s_trailing_space:
                    return False
                
                # sign cannot be the last char,
                # which mean s_integer and s_decimal
                # cannot both be False in the end to
                # be a valid number
            
            elif c.isdigit():
                if s_exponent_pending:
                    s_exponent = True
                    s_exponent_pending = False
                
                s_heading_space = False
                if s_trailing_space:
                    return False
                
                if not s_decimal:
                    s_integer = True
                if s_dot:
                    s_dot = False
                    s_decimal = True
                
                s_signed = True
            
            elif c == '.':
                # '.' may only appear once and
                # it's not allowed in exponent
                if (s_dot or s_decimal or s_exponent
                        or s_exponent_pending):
                    return False
                
                # '.' cannot be the single char
                # besides the sign
                if s_integer:
                    s_decimal = True
                else:
                    # '.' is the first char; if either
                    # s_integer or s_decimal is True
                    # in the end, s_dot will be False
                    s_dot = True
                
                s_heading_space = False
                if s_trailing_space:
                    return False
                
                s_signed = True
            
            elif c == 'e':
                # 'e' cannot be the first char
                if not s_decimal and not s_integer:
                    return False
                
                # 'e' cannot be the last char and
                # may only appear once
                if s_exponent_pending or s_exponent:
                    return False
                s_exponent_pending = True
                
                # exponent may has its own sign
                s_signed = False
                
                s_heading_space = False
                if s_trailing_space:
                    return False
            
            else:
                return False
        
        if not s_exponent_pending and (s_integer or s_decimal):
            return True
        return False
