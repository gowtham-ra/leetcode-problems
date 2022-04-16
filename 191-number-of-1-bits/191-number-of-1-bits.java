public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int count = 0;
        String binaryNo = Integer.toBinaryString(n);
        for (char numChar : binaryNo.toCharArray()) {
            if (numChar == '1') count++;
        }
        return count;        
    }
}