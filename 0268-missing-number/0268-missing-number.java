class Solution {
    public int missingNumber(int[] nums) {
        int total = 0;
        int current_total = 0;
        for (int i = 0; i < nums.length + 1; i++) {
            total += i;
        }
        for (int j = 0; j < nums.length; j++) {
            current_total += nums[j];
        }
        return total - current_total;
    }
}