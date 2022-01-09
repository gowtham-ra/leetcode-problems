# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:        
        if not root:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            #case 1: No children
            if not root.left and not root.right: 
                root = None
            #case 2: 1 child on right
            elif root.right:
                root.val = self.successor(root.right)
                root.right = self.deleteNode(root.right, root.val)
                
            #case 2: 1 child on left
            elif root.left:
                root.val = self.predecessor(root.left)
                root.left = self.deleteNode(root.left, root.val)               
            #case 3: 2 children
            else:
                root.val = self.successor(root.right)                
                root.right = self.deleteNode(delete_node, root.val)   
                        
        return root
    
    def successor(self, node):
        while node.left:
            node = node.left
        
        return node.val
    
    def predecessor(self, node):
        while node.right:
            node = node.right
        
        return node.val
        
        
            
        
        