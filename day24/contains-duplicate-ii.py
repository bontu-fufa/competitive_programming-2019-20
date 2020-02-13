#https://leetcode.com/problems/contains-duplicate-ii

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        d = {}
        
        
        for i in  range(len(nums)):
            
            if nums[i] in d and i - d[nums[i]] <= k:
                    return True
    
            else:
        
                d[nums[i]] = i
        return False
    
    
print(Solution().containsNearbyDuplicate([1,2,3,1,2,3],2))
print(Solution().containsNearbyDuplicate( [1,0,1,1],1))
