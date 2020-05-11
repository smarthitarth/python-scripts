# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:20:23 2020
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
@author: hitarth
"""

def subarraySum(nums, k):
    count = 0
    for start in range(len(nums)):
        sum = 0
        for end in range(start, len(nums)):
            sum += nums[end]
            if(sum==k):
                count+=1
    return count
nums = [1,1,1]
k = 2
print(subarraySum(nums, k))





