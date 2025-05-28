class Solution {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Integer> seen = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (seen.containsKey(nums[i])) {
                return true;
            }
            seen.put(nums[i], 0);
        }
        return false;
    }
}