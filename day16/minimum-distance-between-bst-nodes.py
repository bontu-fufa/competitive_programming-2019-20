
#https://leetcode.com/problems/minimum-distance-between-bst-nodes
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def inorder(root):
            if root is not None:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
                           
        res = []
        inorder(root)
        
        
        minimum  = res[1]-res[0]
        for i in range(1,len(res)-1):
            minimum = min(minimum,(res[i+1]-res[i]))
            
        return minimum
