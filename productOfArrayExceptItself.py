# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 14:52:56 2020
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
@author: hitarth
"""


class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        mulLeft = [0] * n
        mulRight = [0] * n
        pr = [0] * n
        mulLeft[0] = 1
        mulRight[n-1] = 1
        for i in range(1, n):
            mulLeft[i] = nums[i-1] * mulLeft[i-1] 
        for i in range(n-2,-1,-1):
            mulRight[i] = nums[i+1] * mulRight[i+1]
        for i in range(n):
            pr[i] = mulLeft[i] * mulRight[i]
        return pr