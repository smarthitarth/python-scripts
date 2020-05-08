# -*- coding: utf-8 -*-
"""
Created on Fri May  8 08:35:28 2020

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
@author: hitarth
"""
grid1 = [[1,0,1,1,1],[1,0,1,0,1],[1,1,1,0,1]]

       
def numIslands(grid):
    rows = len(grid)
    columns = len(grid[0])
    print(rows, columns)
    islands = 0
       
    if(grid==None or rows == 0 or columns == 0 ): return 0
   
    for i in range(rows):
        for j in range(columns):
            if(grid[i][j]==1):
                islands += 1
                merge(grid, i, j)
                print(grid)
    return islands

def merge(grid, i, j):
    rows = len(grid)
    columns = len(grid[0])
        
    if(i<0 or i>=rows or j<0 or j>=columns or grid[i][j]!=1): return
        
    grid[i][j] = -1
        
    merge(grid, i-1, j)
    merge(grid, i+1, j)
    merge(grid, i, j-1)
    merge(grid, i, j+1)

print(numIslands(grid1))
    
    
        
        