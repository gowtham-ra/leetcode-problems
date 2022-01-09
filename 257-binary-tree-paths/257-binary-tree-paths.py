# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.answer = []
        self.path = []
        self.paths(root)
        return self.answer
        
    def paths(self, node):
        if not node:
            return

        self.path.append(str(node.val))
        
        if not node.left and not node.right:
            self.answer.append('->'.join(self.path))
            self.path.pop()
            return
                
        
        self.paths(node.left)
        self.paths(node.right)

        self.path.pop()
        
        return


        
        
        