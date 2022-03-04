# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = head 
        if prev is None:
            return head
        
        cur = prev.next
        while cur:
            if cur.val == prev.val:
                prev.next = cur.next
                cur = cur.next
            else:
                prev = prev.next
                cur = cur.next
        
        return head
                
                
                
                
            
        