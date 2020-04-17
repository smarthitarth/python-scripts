# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 21:45:01 2020

@author: hitar
"""


arr = [1,1,2,2]
c = 0
for i in arr:
    if i+1 in arr:
        c+=1
print(c)

