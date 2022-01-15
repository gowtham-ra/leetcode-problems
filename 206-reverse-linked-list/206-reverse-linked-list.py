# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        
        if head.next is None:
            return head
        
        rev_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return rev_head
        
            
        
#         if head is None:
#             return head
        
#         if head.next is None:
#             rev_head = head
#             return rev_head

#         rev_head = self.reverseList(head.next)

#         head.next.next = head
#         head.next = None
#         return rev_head

