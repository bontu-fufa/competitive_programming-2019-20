#https://leetcode.com/problems/rotting-oranges
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        column = len(grid[0])
        
        fresh = 0
        queue = deque()
        
        for r in range(row):
            for c in range(column):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh+=1
        if not fresh : return 0
        minutes = 0  
        adjacents = [(0,1),(0,-1),(1,0),(-1,0)]

        while queue and fresh > 0:
            
            minutes += 1
            for _ in range(len(queue)):
                currentX,currentY = queue.popleft()
                for x,y in adjacents:
                    newX = currentX + x
                    newY = currentY + y
                    if 0 <= newX < row and 0 <= newY < column and  grid[newX][newY] == 1 :
                        grid[newX][newY] = 2
                        fresh -= 1
                        queue.append((newX,newY))
          
        if fresh : return -1
        return minutes
