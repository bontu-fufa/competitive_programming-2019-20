#https://leetcode.com/problems/powerful-integers/
from math import log, ceil

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        
        res = set()
        if x == 1 and y ==1 :
            if bound > 1:
                return [2]
            else:
                return []
        
        if x == 1 and y > 1:
            currentY = ceil(log(bound,y))
            currentX = currentY
        elif x > 1 and y == 1:
            currentX = ceil(log(bound,x))
            currentY = currentX
        else:
            currentX = ceil(log(bound,x))
            currentY = ceil(log(bound,y))
        
        for i in range(currentX):
            for j in range(currentY):
                prodsum = x**i + y**j 
                if prodsum <= bound and prodsum not in res:
                    res.add(prodsum)
                    
        return list(res)
