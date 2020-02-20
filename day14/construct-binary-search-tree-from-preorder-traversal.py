#https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        
        if not preorder: return None 
        
        bst = TreeNode(preorder[0])
        
        i = 1
        while i < len(preorder):
            if preorder[i] > preorder[0]:
                break
            i += 1
            
        bst.left = self.bstFromPreorder(preorder[1:i])
        bst.right = self.bstFromPreorder(preorder[i:])
        
        return bst
