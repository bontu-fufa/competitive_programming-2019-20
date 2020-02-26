#https://leetcode.com/problems/all-elements-in-two-binary-search-trees
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        
        def inorder(root,rootArr):
            if root:
                inorder(root.left,rootArr)
                rootArr.append(root.val)
                inorder(root.right,rootArr)
                
        root1Arr = []

        inorder(root1,root1Arr)
        inorder(root2,root1Arr)
   
        return sorted(root1Arr)
