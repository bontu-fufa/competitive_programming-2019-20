#https://leetcode.com/problems/binary-tree-level-order-traversal-ii
from collections import deque 
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        
        levelOrderedNodes = []
        queue = deque()
        queue.append(root)
        
        while queue:
            size = len(queue)
            currentLevel = []
            for _ in range(size):
                node = queue.popleft()
                currentLevel.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levelOrderedNodes.append(currentLevel)               
        return levelOrderedNodes[::-1]
