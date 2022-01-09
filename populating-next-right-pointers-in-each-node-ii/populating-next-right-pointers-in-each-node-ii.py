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
    def processChild(self, childnode, prev, leftmost):
        if childnode:
            if prev:
                prev.next = childnode
            else:
                leftmost = childnode
            
            prev = childnode
                
        return prev, leftmost
    
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        leftmost = root
        
        while leftmost:
            prev = None
            cur = leftmost
            leftmost = None
            
            while cur:
                prev, leftmost = self.processChild(cur.left, prev, leftmost)
                prev, leftmost = self.processChild(cur.right, prev, leftmost)
                
                cur = cur.next
            
        return root
                