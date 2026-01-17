class Solution {
    public int maxArea(int[] height) {
        int l = 0, r = height.length - 1;
        int max_area = 0;
        while (l < r) {
            max_area = Math.max(max_area, Math.abs(l - r) * (Math.min(height[l], height[r])));
            if (height[l] < height[r]) {
                l++;
            } else {
                r--;
            }
        }
        return max_area;
    }
}