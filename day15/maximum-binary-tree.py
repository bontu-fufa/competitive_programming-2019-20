#https://leetcode.com/problems/maximum-binary-tree
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
    
        if not nums : return None 
        
        maxEle = max(nums)
        ind = nums.index(maxEle)
        
        tree = TreeNode(maxEle)
        tree.left = self.constructMaximumBinaryTree(nums[:ind])
        tree.right = self.constructMaximumBinaryTree(nums[ind+1:])
        
        return tree
