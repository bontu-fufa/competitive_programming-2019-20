#https://leetcode.com/contest/weekly-contest-176/problems/count-negative-numbers-in-a-sorted-matrix
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        negatives  = 0
                
            
            
            
#         O(n*m)
        if grid == [[]]: return 0
        
        for i in range(m-1,-1,-1):
            for j in range(n):
                if grid[i][j] < 0:
                
                    negatives += n - j
                    break
        return negatives
        
        
        
        
        
#         O(n+m)    
        row = 0
        column = n-1

        while 0 <= row < m and 0 <= column < n :
            
            if grid[row][column] < 0:
                negatives += m - row
                column -= 1
            else: 
                row += 1
                
        return negatives

