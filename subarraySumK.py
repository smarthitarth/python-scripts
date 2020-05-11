# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:09:45 2020
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
@author: hitarth
"""


def subarraySum(nums, k):
    count = 0
    sum = [0] * (len(nums)+1)
    
    
    for i in range(1, len(nums)+1):
        sum[i] = sum[i-1] + nums[i-1]
        print(sum)
    for start in range(len(nums)):
        for end in range(start+1, len(nums)+1):
            if(sum[end]-sum[start]==k):
                count+=1
    return count

nums = [1,1,1]
k = 2
print(subarraySum(nums, k))


            