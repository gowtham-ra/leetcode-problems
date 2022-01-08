# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def symmetric(rootA, rootB):
            if not rootA and not rootB:
                return True
            elif not rootA or not rootB:
                return False
            
            if rootA.val != rootB.val:
                return False
                
            left = symmetric(rootA.left, rootB.right)
            right = symmetric(rootA.right, rootB.left)
            
            return left and right
        
        return symmetric(root.left, root.right)
                
        
        
    
            

            

        
        
        