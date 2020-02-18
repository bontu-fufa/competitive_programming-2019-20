#https://leetcode.com/problems/h-index-ii
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if(len(citations) == 0):
            return 0;
        
        passed = 1
        
        for i in range(len(citations)-1,-1,-1):
            if citations[i] < passed:
                return passed - 1
            elif citations[i] == passed:
                return passed
            else:
                passed += 1
                
        return passed - 1;
