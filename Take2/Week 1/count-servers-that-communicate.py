#https://leetcode.com/problems/count-servers-that-communicate/submissions/

def countServers(self, grid: List[List[int]]) -> int:
        row,column = len(grid),len(grid[0])
        visited = set()
        
        def neighborServers(r,c):
            neighbors = set()
            for i in range(column):
                if grid[r][i] == 1:
                    neighbors.add((r,i))
            for j in range(row):
                if grid[j][c] == 1:
                    neighbors.add((j,c))
            neighbors.remove((r,c))
            return neighbors
       
        def serversInCommunication(r,c):
            neighbors = neighborServers(r,c)
            for n in neighbors:
                nRow,nCol =  n
                if (nRow,nCol) not in visited and grid[nRow][nCol] == 1:
                    visited.add((nRow,nCol))
                    
        
        
        for r in range(row):
            for c in range(column):
                if grid[r][c] == 1 :
                    serversInCommunication(r,c)
        return len(visited)
        
