class Solution {
    public int[] productExceptSelf(int[] nums) {
        int prod = 1;
        int zero_counter = 0;
        for (int num : nums) {
            if (num != 0) {
                prod *= num;
            } else {
                zero_counter++;
            }
        }
        if (zero_counter > 1) {
            return new int[nums.length];
        } 
        for (int i = 0; i < nums.length; i++) {
            if (zero_counter == 1) {
                if (nums[i] == 0) {
                    nums[i] = prod;
                } else {
                    nums[i] = 0;
                } 
            } else {
                nums[i] = prod / nums[i];
            }
        }
        return nums;
    }
}