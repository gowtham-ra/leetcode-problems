class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int answer = 0;
        int localCount = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                localCount++;
            } else {
                answer = Math.max(localCount, answer);
                localCount = 0;
            }
        }
        answer = Math.max(localCount, answer);        
        return answer;
    }
}