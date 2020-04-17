# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 22:27:18 2020

@author: hitar
"""
def rev(s):
    l = sorted(s, reverse = True)
    l[0] = l[0] - l[1]
    l.pop(1)
    return(l)
stones = [2,7,4,1,8,1]
while(len(stones) != 1):
    stones = rev(stones)
print("Last Stone Weight: " , stones[0])


import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new_list = [-x for x in stones]
        heapq.heapify(new_list)
        while len(new_list) > 1:
            y = heapq.heappop(new_list)
            x = heapq.heappop(new_list)
            if y != x:
                heapq.heappush(new_list, y-x)
        if len(new_list):
            return -heapq.heappop(new_list)
        return 0