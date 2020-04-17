# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 16:45:32 2020

@author: hitar
"""
import collections
nums = [0,0,1]

c = 0
l = len(nums)
co = collections.Counter(nums)
for i in range(co[0]):
    nums.remove(0)
for i in range(co[0]):
    nums.append(0)
print(nums)