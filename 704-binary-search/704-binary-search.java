class Solution {
    private static int[] nums;
    
    public int search(int[] nums, int target) {
        this.nums = nums;
        return binSearch(0, nums.length-1, target);
    }
    
    private static int binSearch(int low, int high, int target) {
        if (low > high) return -1;
        
        int mid = low + (high - low) / 2;
        int midVal = nums[mid];
        if (midVal < target) return binSearch(mid+1, high, target);
        else if (midVal > target) return binSearch(low, mid-1, target);
        
        return mid;            
    }
}