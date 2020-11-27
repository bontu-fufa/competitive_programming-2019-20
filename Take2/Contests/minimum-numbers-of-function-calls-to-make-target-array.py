#https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        count = 0
        isAllZero = True
        
        while True:
            
            for i in range(len(nums)):
                if nums[i] % 2 != 0 :
                    nums[i] -= 1
                    count += 1
                nums[i] //= 2
                if nums[i] != 0 : 
                    isAllZero = False
            if isAllZero : 
                return count
            isAllZero = True
            count += 1
