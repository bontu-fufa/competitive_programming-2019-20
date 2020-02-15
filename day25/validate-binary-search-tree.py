#https://leetcode.com/problems/validate-binary-search-tree
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        ordered = []
        def inorder(root):
            if root is not None:
                inorder(root.left)
                ordered.append(root.val)
                inorder(root.right)
            
        inorder(root)
        
        for i in range(len(ordered)-1,0,-1):
            if ordered[i] <= ordered[i-1]:
                return False
        return True
