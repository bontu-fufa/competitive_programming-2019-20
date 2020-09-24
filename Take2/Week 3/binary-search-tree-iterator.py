#https://leetcode.com/problems/binary-search-tree-iterator
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.elements = []
        self.reversedInorder(root)
        
    def reversedInorder(self,root):
        if root:
            self.reversedInorder(root.right)
            self.elements.append(root.val)
            self.reversedInorder(root.left)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.elements.pop()
    
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.elements != []
