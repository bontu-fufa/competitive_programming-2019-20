#https://leetcode.com/problems/play-with-chips
class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        
        oddpossition , evenposition = 0,0
        for chip in chips:
            if chip%2 != 0 : oddpossition +=1 
            else : evenposition += 1
        return min(evenposition,oddpossition)
