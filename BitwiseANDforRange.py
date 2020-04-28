# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:05:29 2020
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

@author: hitarth
"""
def msb(n):
    msb_p = -1
    while (n>0):
        n = n >> 1
        msb_p += 1
    return msb_p

def andOp(x, y):
    res = 0 # Initialize result
    
    while (x>0 and y>0):
        #find pos in MSB in x and y
        msb_1 = msb(x)
        msb_2 = msb(y)
        
        #if bits are different then return
        if(msb_1 != msb_2):
            break
        #adding 2^msb_1 to result
        msb_val = (1 << msb_1)
        res += msb_val
        
        #subtract 2^msb_1 from x and y
        x -= msb_val
        y -= msb_val
    return res

print(andOp(10, 15))

"""
# An efficient Python3 program to find  
# bit-wise & of all numbers from x to y.  
def andOperator(a, b): 
    while(a < b): 
          
        # -b is the 2's complement of b  
        # when do bitwise or with b we 
        # get LSB and we subtract that from b  
        b -= (b & -b)  
    return b  
  
# Driver code  
a, b = 10, 15
print(andOperator(a, b)) 
  
# This code is contributed by  
# Shubham Singh (SHUBHAMSINGH10) 
"""