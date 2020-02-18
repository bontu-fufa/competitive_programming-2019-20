#https://leetcode.com/problems/binary-search

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        initialPnt = 0
        finalPnt = len(nums)-1
        while initialPnt <= finalPnt:
            
            mid = (initialPnt + finalPnt) // 2
            if target == nums[mid]:
                return mid
            elif  target< nums[mid]:
                finalPnt = mid -1
            else :
                initialPnt = mid + 1
        return -1
    
