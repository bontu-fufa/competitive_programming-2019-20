#https://leetcode.com/problems/binary-tree-postorder-traversal
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root: return []
        
        stack = [root]
        ordered = []
        
        while stack:
            currentNode = stack.pop()
            ordered.append(currentNode.val)
            if currentNode.left : stack.append(currentNode.left)
            if currentNode.right : stack.append(currentNode.right)
                
        return ordered[::-1]
