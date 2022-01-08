from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        que = deque()
        
        if root is None:
            return ans
        
        que.append(root)
        
        while (que):   
            length = len(que)
            ans_lvl = []     
            for i in range(length):
                cur = que.popleft()
                ans_lvl.append(cur.val)            
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            
            ans.append(ans_lvl)
        
        return ans
              
        