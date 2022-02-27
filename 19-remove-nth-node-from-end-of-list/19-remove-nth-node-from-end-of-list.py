# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:        
        if head is None:
            return 0
        elif head.next is None and n == 1: 
            head = None
            return head
        
        def remove(node):
            if node is None:
                return 0
            
            count = 1 + remove(node.next)
            
            if count == n+1:
                node.next = node.next.next
            
            return count
        
        count = remove(head)
        
        if count == n:
            return head.next
        
        return head
    