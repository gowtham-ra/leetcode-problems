# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [(root, False)]
        answer = []

        while stack:
            node, visited = stack.pop()

            if node:
                if visited:
                    answer.append(node.val)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        
        return answer
    
#         answer = []
        
#         stack = [root]
        
        
#         while stack:
#             node = stack.pop()
            
#             if node:
#                 answer.append(node.val)
            
#                 if node.left:
#                     stack.append(node.left)
#                 if node.right:
#                     stack.append(node.right)
        
#         return answer[::-1]
        