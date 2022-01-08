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
        
        def symmetric(left, right):
            if left is None and right is None:
                return True
            elif left is None or right is None:
                return False
            
            if left.val != right.val:
                return False
            a = symmetric(left.left, right.right)
            b = symmetric(left.right, right.left)

            return a and b
        
        return symmetric(root.left, root.right)
        