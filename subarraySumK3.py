# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:31:10 2020
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
@author: hitarth
"""



def subarraySum(nums, k):
    count = 0
    sum = 0
    map = dict()
    map[0]=1
    
    for i in range(len(nums)):
        sum += nums[i]
        if(map.get(sum - k, 0)):
            count += map.get(sum - k)
        map[sum] = map.get(sum, 0)+1
    return count
nums = [1,1,1]
k = 2
print(subarraySum(nums, k))




class Solution:
    def subarraySum2(self, nums: List[int], k: int) -> int:
        total = 0
        sum_freq = {}
        sum_freq[0] = 1
        s = 0
        for n in nums:
            s += n
            if (s - k) in sum_freq:
                total += sum_freq[s - k]
            if s in sum_freq:
                sum_freq[s] += 1
            else:
                sum_freq[s] = 1
                
        return total