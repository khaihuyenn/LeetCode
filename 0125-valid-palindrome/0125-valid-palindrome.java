class Solution {
    public boolean isPalindrome(String s) {
        String cleaned_s = s.toLowerCase().replaceAll("[^a-zA-Z0-9]", "");
        int left = 0, right = cleaned_s.length() - 1;
        char [] charArray = cleaned_s.toCharArray();
        if (charArray.length == 0) {
            return true;
        }
        while (left < right) {
            if (charArray[left] == charArray[right]) {
                left++;
                right--;
            } else {
                return false;
            }
        }
        return true;
    }
}