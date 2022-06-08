# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            new_head = head
            return new_head
        
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return new_head
        
                
        