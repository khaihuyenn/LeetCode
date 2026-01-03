class Solution {
    public boolean isAnagram(String s, String t) {
        int[] counter = new int[26];
        for (char c : s.toCharArray()) {
            counter[c - 'a']++;
        }
        for (char c : t.toCharArray()) {
            counter[c - 'a']--;
        }
        for (int i : counter) {
            if (i != 0) {
                return false;
            }
        }
        return true;
    }
}