1. Unable to Find Approach for O(1) space --> not using queues
2. You can solve by traversing as linkedlist using already set next pointers in cur level
3. You should have following pointers
* cur  = cur node of the linkedlist (cur level)
* prev = cur child that is being pointed to
* leftmost = leftmost node of the next level
4. You should also include one more helper function (childnode, prev, leftmost)
5. TC: O(n) SC: O(1)