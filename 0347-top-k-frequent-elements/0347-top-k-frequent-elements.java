class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        List<Integer>[] freq = new List[nums.length + 1];
        for (int i = 0; i < nums.length + 1; i++) {
            freq[i] = new ArrayList<>();
        }

        Map<Integer, Integer> counter = new HashMap<>();
        for (int num : nums) {
            counter.putIfAbsent(num, counter.getOrDefault(num, 0) + 1);
        }
        for (Map.Entry<Integer, Integer> entry : counter.entrySet()) {
            freq[entry.getValue()].add(entry.getKey());
        }
        int[] result = new int[k];
        int index = 0;
        for (int i = freq.length - 1; i > 0; i--) {
            for (int n : freq[i]) {
                result[index] = n;
                index++;
                if (index == k) {
                    return result;
                }
            }
        }
        return result;
    }
}