class Solution {
    public double average(int[] salary) {
        int count = salary.length - 2;
        int sum = 0;
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        
        for (int value : salary) {
            if (value < min) min = value;
            if (value > max) max = value;
        }
        
        for (int value : salary) if (value != min && value != max) sum += value;        
        double average = (double) sum / count;
        return average;
    }
}