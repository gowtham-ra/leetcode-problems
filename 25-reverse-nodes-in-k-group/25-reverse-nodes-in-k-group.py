# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:        
        if k == 1:
            return head
            
        kTail = None        
        ptr = head
        new_head = None
        
        while ptr:
            count = 0
            
            ptr = head
            while count < k and ptr:
                ptr = ptr.next
                count += 1
            
            if count == k:
                revHead = self.reverseLL(head, k)
                
                if not new_head:
                    new_head = revHead
                
                if kTail:
                    kTail.next = revHead
                
                kTail = head
                head = ptr
        
        if kTail:
            kTail.next = head
        
        return new_head if new_head else head
        
        
    def reverseLL(self, head, k):
        new_head, ptr = None, head
        
        while k:
            next_node = ptr.next
            
            ptr.next = new_head
            new_head = ptr
            
            ptr = next_node
            k -= 1
        
        return new_head
