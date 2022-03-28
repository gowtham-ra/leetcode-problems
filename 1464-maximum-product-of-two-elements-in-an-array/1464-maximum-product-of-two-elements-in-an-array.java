import java.util.*;

class Solution {
    public int maxProduct(int[] nums) {
       Queue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);
        for (int num : nums)
            pq.add(num);
        int num1 = pq.poll();
        int num2 = pq.poll();

        return (num1 - 1) * (num2 - 1);        
    }
}