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
    public ListNode deleteNodes(ListNode head, int m, int n) {
        ListNode prev = head;
        ListNode cur = head;
        int count = 0;
        
        while (cur != null) {
            count = 0;
            while (cur != null && count < m) {
                count++;
                prev = cur;
                cur = cur.next;
            }
            
            count = 0;
            while (cur != null && count < n) {
                count++;
                cur = cur.next;
            }            
            prev.next = cur;
        }
        
        return head;
    }
}