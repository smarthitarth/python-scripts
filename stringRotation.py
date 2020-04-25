# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 14:00:29 2020
String rotation
@author: hitarth
"""
def leftRot(s, n):
    return s[n:] + s[:n]
print(leftRot('abcdefg', 3))
print(leftRot('abcdefg', 4))