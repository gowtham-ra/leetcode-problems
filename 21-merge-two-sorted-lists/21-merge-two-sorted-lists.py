# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()
        itr = new_head
        self.merge(itr, list1, list2)
        
        return new_head.next
    
    def merge(self, itr, list1, list2):
        if list1 and list2:
            if list1.val <= list2.val:
                itr.next = list1
                self.merge(itr.next, list1.next, list2)
            else:
                itr.next = list2
                self.merge(itr.next, list1, list2.next)
        elif list1:
            itr.next = list1
            self.merge(itr.next, list1.next, list2)
        elif list2:
            itr.next = list2
            self.merge(itr.next, list1, list2.next)
            
        