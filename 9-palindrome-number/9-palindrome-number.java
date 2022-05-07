class Solution {
    public boolean isPalindrome(int x) {
        String numStr = Integer.toString(x);
        int start = 0;
        int end = numStr.length()-1;
        
        while (start < end) {
            if (numStr.charAt(start) != numStr.charAt(end)) {
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
}