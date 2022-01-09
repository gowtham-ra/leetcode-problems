# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        mini = float('-inf')
        maxi = float('inf')
        return self.validBST(root, mini, maxi)
        
    
    def validBST(self, root, mini, maxi):
        if not root:
            return True
        
        if root.val >= maxi or root.val <= mini:
            return False
        
        left = self.validBST(root.left, mini, root.val)
        right = self.validBST(root.right, root.val, maxi)
        
        return left and right
        
        
