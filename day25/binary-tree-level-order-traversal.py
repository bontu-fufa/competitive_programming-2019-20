#https://leetcode.com/problems/binary-tree-level-order-traversal
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root: return []
        levels =[]
        
        #BFS
        
        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue) 
            currentLevel = []
            
            for node in range(size):
                currentNode = queue.popleft()
                currentLevel.append(currentNode.val)
                
                if currentNode.left:
                    queue.append(currentNode.left)
                    
                    
                if currentNode.right:
                    queue.append(currentNode.right)
                    
            levels.append(currentLevel)
                
        
        return levels
        
        #O(N) -- time
        #O(N)-- space
         
