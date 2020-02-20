#https://leetcode.com/problems/insert-into-a-binary-search-tree

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root : return TreeNode(val)

        else:
            if val > root.val:
                if root.right is None:
                    root.right = TreeNode(val)
                else:
                    self.insertIntoBST(root.right,val)
            else:
                if root.left is None:
                    root.left = TreeNode(val)
                else:
                    self.insertIntoBST(root.left,val)
            return root
