class Solution(object):
    def topKFrequent(self, nums, k):
        # Count frequencies using a hashmap
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        # BucketSort the number based on their frequencies
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in counter.items():
            bucket[freq].append(num)
        # Collect the top k frequent elements
        res = []
        for i in range(len(nums), 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res