#https://leetcode.com/problems/friend-circles

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def dfs(i):
            for j in range(len(M)):
                if not visited[j] and j != i and M[i][j] == 1:
                    visited[j] = True
                    dfs(j)
            
        if len(M) == 0 : return 0
        friends = 0
        visited = [False]*len(M)
        for i in range(len(M)):
            if not visited[i]:
                friends += 1
                visited[i] = True 
                dfs(i)
        return friends
