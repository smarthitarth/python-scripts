# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 16:45:29 2020
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
@author: hitarth
"""

nums = [4,5,6,7,0,1,2]
target = 6
    
def search(nums, target):    
    if(nums == None or len(nums) == 0): return -1
    
    l = 0;
    r = len(nums)-1
    
    while(l<r):
        mid = l+(r-l)//2
        if(nums[mid]>nums[r]):
            l = mid+1
        else:
            r = mid
    print('1l:', l)
    print('r:', r)
    start = l
    l = 0
    r = len(nums)-1
    
    if((target>=nums[start]) & (target<=nums[r])):
        l=start
    else:
        r=start
    print('2l:', l)
    print('r:', r)
    
    while(l<=r):
        mid = l+(r-l)//2
        print("mid:", mid)
        if(nums[mid]==target):
            return mid
        elif(nums[mid]<target):
            l=mid+1
        else:
            r=mid-1
        print('3l:', l)
        print('r:', r)
    return -1
print(search(nums, target))