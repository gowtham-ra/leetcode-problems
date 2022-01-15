# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         head = None
        
#         if l1 is None and l2 is None:
#             return head
#         elif l1 is None:
#             head = l2
#             return head
#         elif l2 is None:
#             head = l1
#             return head
        
#         i1 = l1
#         i2 = l2
        
#         if l1.val < l2.val:
#             head = l1
#             i1 = i1.next
#         else:
#             head = l2
#             i2 = i2.next
        
#         cur = head
        
#         while i1 and i2:
#             if i1.val <= i2.val:
#                 cur.next = i1
#                 i1 = i1.next
#             else:
#                 cur.next = i2
#                 i2 = i2.next
            
#             cur = cur.next
        
#         while i1:
#             cur.next = i1
#             i1 = i1.next
#             cur = cur.next

#         while i2:
#             cur.next = i2
#             i2 = i2.next
#             cur = cur.next
        
#         return head
            
            
        
        
        
        