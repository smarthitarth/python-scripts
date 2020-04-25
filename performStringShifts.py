# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 14:12:28 2020
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

direction can be 0 (for left shift) or 1 (for right shift). 
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.
@author: hitar
"""


def stringShift(s: str, shift) -> str:
        def leftRot(s, n):
            return s[n:] + s[:n]
        sum = 0
        for i in shift:
            if(i[0] == 0):
                sum -= i[1]
            else:
                sum += i[1]
        print(sum)
        if(sum < 0):
            return(leftRot(s, abs(sum)%len(s)))
        else:
            return(leftRot(s, len(s) - sum%len(s)))
        return s
s = "xqgwkiqpif"
shift = [[1,4],[0,7],[0,8],[0,7],[0,6],[1,3],[0,1],[1,7],[0,5],[0,6]]
print(stringShift(s, shift))