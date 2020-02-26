#https://leetcode.com/problems/maximum-subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        dp = [0]*len(nums)
        dp[0] = nums[0]
        
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1] + nums[i],nums[i])
            maxSub = max(dp[i],maxSub)
        return maxSub
