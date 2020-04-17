# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 19:58:58 2020

@author: hitar
"""

nums = [-2,1,-3,4,-1,2,1,-5,4]
su = -1000000
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        su = max(su, sum(nums[i:j]))
        
print(su)