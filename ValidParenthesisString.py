# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 15:12:48 2020
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
@author: hitar
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        l_b = 0
        for c in s:
            if c in "(*":
                l_b += 1
            else:
                l_b -= 1
            if l_b < 0:
                return False
        r_b = 0
        for c in reversed(s):
            if c in ")*":
                r_b += 1
            else:
                r_b -= 1
            if r_b < 0:
                return False
            
        return True
    
    
"""
class Solution:
    def checkValidString(self, s: str) -> bool:
        lo,hi=0,0
        for c in s:
            lo += 1 if c=='(' else -1 # treat '*' as ')'
            hi += 1 if c!=')' else -1 # treat '*' as '('
            lo = max(lo, 0)  # treat '*' as empty
            if hi<0: return False # ')' more than '*'+'('
        return lo==0 # detect if more '(' than '*'
    
"""