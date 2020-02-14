#https://leetcode.com/problems/binary-tree-right-side-view

from collections import deque
class Solution:

    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        rightSide = []
        
        que = deque()
        que.append(root)
        
        while que:
            size = len(que)
            last = size - 1
            for i in range(size):
                top = que.popleft()
                if i == last:
                    rightSide.append(top.val)
                if top.left:
                    que.append(top.left)
                    
                if top.right:
                    que.append(top.right)
        
        return rightSide
