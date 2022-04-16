class Solution {
    public int[] sortedSquares(int[] nums) {
        int[] answerArr = new int[nums.length];
        int left = 0;
        int right = nums.length - 1;     
        
        for (int i = right; i >= 0; i--) {
            int val1 = nums[left] * nums[left];
            int val2 = nums[right] * nums[right];
            if (val1 < val2) {
                answerArr[i] = val2;
                right--;                
            } else {
                answerArr[i] = val1;
                left++;
            }
        }
        return answerArr;
    }
}