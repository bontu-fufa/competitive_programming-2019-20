#https://leetcode.com/problems/perfect-number

from math import sqrt
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # sum = 0
        # for i in range(1,int(sqrt(num))):
        #     if num%i == 0:
        #         sum += i
        # return sum == num
        if num < 6:
            return False
        sum = 1
        for i in range(2,int(sqrt(num)+1)):
            if num%i == 0:
                other = num//i
                sum += (i + other)
                
        return sum == num
    
# print(Solution().checkPerfectNumber(6))
        
        
        
             
                
