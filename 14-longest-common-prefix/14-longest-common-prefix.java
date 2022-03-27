class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0)
            return "";        
        
        int minLen = Integer.MAX_VALUE;
        for (String str: strs) {
            minLen = Math.min(str.length(), minLen);
        }
        
        int low = 1;
        int high = minLen;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (isCommonPrefix(strs, mid))
                low = mid + 1;
            else
                high = mid - 1;
        }
        
        int mid = ((low + high) / 2);
        return strs[0].substring(0, mid);
    }
    
    private boolean isCommonPrefix(String[] strs, int len) {
        String substr = strs[0].substring(0, len);
        for (int i = 1; i < strs.length; i++)
            if (!strs[i].startsWith(substr))
                return false;        
        return true;
    }
}