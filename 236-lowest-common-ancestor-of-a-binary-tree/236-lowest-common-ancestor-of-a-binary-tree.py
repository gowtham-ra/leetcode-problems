# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack1 = []
        stack2 = []
        
        self.find(root, p, stack1)
        self.find(root, q, stack2)
        
        len1 = len(stack1)
        len2 = len(stack2)
        
        if len1 > len2:
            big = stack1
        else:
            big = stack2
        
        count = abs(len1 - len2)
        
        while count > 0:
            big.pop()
            count -= 1
        
        while stack1 and stack2:
            a = stack1.pop()
            b = stack2.pop()
            
            if a == b:
                return a            
        
    def find(self, root, target, stack):
        if not root:
            return False
        
        stack.append(root)
        
        if root.val == target.val:
            return True
        
        left = self.find(root.left, target, stack)        
        
        right = False        
        if not left:
            right = self.find(root.right, target, stack)
        
        if not left and not right:
            stack.pop()
        
        return left or right

        
            
            
        
        