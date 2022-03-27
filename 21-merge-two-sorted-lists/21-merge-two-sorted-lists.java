/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode idx1 = list1;
        ListNode idx2 = list2;
        ListNode head = new ListNode(0);
        ListNode cur = head;
        
        if (list1 == null) 
            return list2;
        else if (list2 == null)
            return list1;
        
        while (idx1 != null && idx2 != null) {
            if (idx1.val < idx2.val) {
                cur.next = idx1;
                idx1 = idx1.next;
            } else {
                cur.next = idx2;
                idx2 = idx2.next;
            }
            cur = cur.next;
        }
        
        while (idx1 != null) {
            cur.next = idx1;
            idx1 = idx1.next;
            cur = cur.next;
        }
        while (idx2 != null) {
            cur.next = idx2;
            idx2 = idx2.next;
            cur = cur.next;
        }        
        
        return head.next;

    }
}