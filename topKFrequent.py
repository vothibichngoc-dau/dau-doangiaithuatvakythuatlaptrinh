class Solution(object):
    def topKFrequent(self, nums, k):
        # 1. Đếm tần suất
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        # 2. Bucket sort theo tần suất
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        
        # 3. Lấy k phần tử có tần suất cao nhất
        res = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res