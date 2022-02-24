# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:        
        k = len(lists)
        if k == 0:
            return None
        
        l1 = lists[0] 
        
        for i in range(1, k):
            head = ListNode()
            cur = head
            
            l2 = lists[i]

            while l1 and l2:        
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next

                cur = cur.next

            if l1:
                cur.next = l1
            elif l2:
                cur.next = l2
            
            l1 = head.next
        
        return l1


