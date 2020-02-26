#https://leetcode.com/problems/min-cost-climbing-stairs
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cost = cost + [0]
        minCost = [0]*len(cost)
        minCost[0] = cost[0]
        minCost[1] = cost[1]
        for i in range(2,len(cost)):
            minCost[i] = cost[i] + min(minCost[i-1],minCost[i-2])
        return minCost[-1]
