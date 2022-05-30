class Solution {
    public String[] findRelativeRanks(int[] score) {
        int maxValue = Arrays.stream(score).max().getAsInt();
        int[] checkArr = new int[maxValue+1];
        Map<Integer, Integer> map = new HashMap<>();


        for (int i = 0; i < score.length; i++) {
            int scr = score[i];
            checkArr[scr]++;
            map.put(scr, i);
        }
        
        int count = 0;
        String[] result = new String[score.length];
        String[] ranks = {"Gold Medal", "Silver Medal", "Bronze Medal"};
        for (int i = checkArr.length-1; i >= 0; i--) {
            if (checkArr[i] == 1 && count < 3) {
                result[map.get(i)] = ranks[count++];
            } else if (checkArr[i] == 1) {
                result[map.get(i)] = String.valueOf(++count);
            }
        }
        return result;
    }
}