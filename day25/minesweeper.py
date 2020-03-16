https://leetcode.com/problems/minesweeper/
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def isInBoundary(x,y):
            return -1 < x < m  and -1 < y < n
        def searchMine(x,y):
            
            if board[x][y] != "E" : return 
            
            neighbors = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
            mine = 0
            for neighborX,neighborY in neighbors:
                newX = x + neighborX
                newY = y + neighborY
                if isInBoundary(newX,newY) and board[newX][newY] == "M" :
                    mine += 1
            if mine: 
                board[x][y] = str(mine)
                return
            else:board[x][y] = "B"

            for neighborX,neighborY in neighbors:
                newX = x + neighborX
                newY = y + neighborY
                if isInBoundary(newX,newY) and (newX,newY) not in visited:
                    visited.add((newX,newY))
                    searchMine(newX,newY)
                    
                    
                    
        if not board : return []
        m = len(board)
        n = len(board[0])
        clickedX = click[0]
        clickedY = click[1]
        
        if board[clickedX][clickedY] == "M":
            board[clickedX][clickedY] = "X"
            return board
        
        visited = set()
        visited.add((clickedX,clickedY))
        searchMine(clickedX,clickedY)
        
        return board
            
        
        
