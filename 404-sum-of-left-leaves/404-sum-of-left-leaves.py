# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        summ = 0
        
        def leafsum(root):
            nonlocal summ
            if root:
                if self.leaf(root.left):
                    summ += root.left.val
                
                leafsum(root.left)
                leafsum(root.right)
        
        leafsum(root)
        return summ
        
    def leaf(self, root):
        if not root:
            return False
        
        return not root.left and not root.right

        