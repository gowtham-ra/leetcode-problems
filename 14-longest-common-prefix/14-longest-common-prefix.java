class Solution {
    public String longestCommonPrefix(String[] strs) {
        int length = Integer.MAX_VALUE;
        
        
        if (strs.length == 1) return strs[0];
        
        for (String word : strs) {
            length = Math.min(length, word.length());
        }
        
        int count = 0;
        boolean done = false;
        outer:
        for (int i = 0; i < length; i++) {
            for (int j = 0; j < strs.length-1; j++) {
                if (strs[j].charAt(i) != strs[j+1].charAt(i)) {
                    done = true;
                    break;
                }
                
                if (j+1 == strs.length-1) count++;
            }
            
            if (done) {
                break;
            }
        }
        
        return strs[0].substring(0, count);
        
    }
}