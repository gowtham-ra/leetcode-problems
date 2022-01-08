from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = deque()
        
        if not root:
            return root
        
        queue.append(root)
        
        while queue:
            length = len(queue)
            
            for i in range(length):
                node = queue.popleft()
                
                if i != (length-1):
                    node.next = queue[0]
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
        
        return root
            
                    
        
        