class Solution {
    public int maxSubArray(int[] nums) {
        int localSum = nums[0];
        int globalSum = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int num = nums[i];
            localSum = Math.max(num, localSum+num);
            globalSum = Math.max(localSum, globalSum);
        }
        return globalSum;  
    }
}