#https://leetcode.com/contest/weekly-contest-176/problems/count-negative-numbers-in-a-sorted-matrix
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        negatives  = 0
        if grid == [[]]: return 0
        
        for i in range(m-1,-1,-1):
            for j in range(n):
                if grid[i][j] < 0:
                    negatives += n - j
                    break
        return negatives
