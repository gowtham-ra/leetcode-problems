class Solution {
    public int countOdds(int low, int high) {
        int numbers = 0;
        int numOdds = 0;
        boolean evenOddFlag = false;
        boolean evens = false;
        
        numbers = high - low + 1;
        numOdds = numbers / 2;
        
        if (numbers % 2 == 0) evenOddFlag = true;
        if (low % 2 == 0 && high % 2 == 0) evens = true;
        if (evenOddFlag || evens)return numOdds;
        else return numOdds + 1;
        
        
        
        
        
    }
}