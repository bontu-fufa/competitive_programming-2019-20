#https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjList = []
        for _ in range(n):
            adjList.append([])
            
        for i,j in edges:
            adjList[i].append(j)
            adjList[j].append(i)
            
        visited = set()
        def dfs(ind):
            time = 0
            visited.add(ind)
            for adj in adjList[ind]:
                if adj not in visited : 
                    adjTime = dfs(adj)
                    if hasApple[adj] or adjTime:
                        time += adjTime + 2
            return time
        
        return dfs(0)
            
            
        

            
        
        
