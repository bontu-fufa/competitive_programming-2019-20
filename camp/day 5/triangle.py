#https://leetcode.com/problems/triangle
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row = len(triangle)
        for i in range(row-2,-1,-1):
            column = len(triangle[i])
            for j in range(column):
                minimumNumber = min(triangle[i+1][j],triangle[i+1][j+1])
                triangle[i][j] += minimumNumber
        return triangle[0][0]
