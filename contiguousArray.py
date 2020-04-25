# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 13:49:30 2020
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.


@author: hitarth
"""


class Solution:
    def findMaxLength(self, nums) -> int:
        for i in range(0, len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        hm = {} #hashmap
        cs = 0  #current sum
        maxLen = 0
        for i in range(len(nums)):
            cs += nums[i]
            if(cs == 0):
                maxLen = i+1
            if cs in hm:
                if maxLen < i - hm[cs]:
                    maxLen = i - hm[cs]
            else:
                hm[cs] = i
        return maxLen
                
print(Solution().findMaxLength([1,0,0,1,0,1,1]))