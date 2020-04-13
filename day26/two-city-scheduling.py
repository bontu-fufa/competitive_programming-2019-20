#https://leetcode.com/problems/two-city-scheduling
import heapq 
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        difference = []
        for i in range(len(costs)):
            costA = costs[i][0]
            costB = costs[i][1]
            difference.append(((costA - costB),i))
    
        heapq.heapify(difference)
        minCost = 0
        
        for i in range(len(costs)):
            index = heapq.heappop(difference)
            if i < len(costs)//2:
                minCost += costs[index[1]][0]
            else:
                minCost += costs[index[1]][1]
        return minCost 
