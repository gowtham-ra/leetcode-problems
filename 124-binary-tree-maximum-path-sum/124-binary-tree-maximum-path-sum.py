# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        self.maxgain(root)
        return self.max_sum
    
    def maxgain(self, node):
        if not node:
            return 0
        
        left = max(self.maxgain(node.left), 0)
        right = max(self.maxgain(node.right), 0)
        
        self.max_sum = max(self.max_sum, left + node.val + right)
        
        return node.val + max(left, right)
        
        
        