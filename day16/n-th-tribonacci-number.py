#https://leetcode.com/problems/n-th-tribonacci-number
class Solution:
    def tribonacci(self, n: int) -> int:
        def tribonacciR(n):
            if n == 0 : return 0
            if result[n]:
                return result[n]
            else:
                result[n] = tribonacciR(n-1) + tribonacciR(n-2) + tribonacciR(n-3) 
                return result[n]
        
        if n == 0: return 0
        if n == 1 or n==2 : return 1
        
    
        result = [0]*(n+1)
        result[0],result[1],result[2] = 0,1,1
        
            
        tribonacciR(n) 
        return result[n]
