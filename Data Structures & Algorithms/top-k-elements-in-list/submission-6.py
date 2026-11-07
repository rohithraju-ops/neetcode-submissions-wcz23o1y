class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        heap = []
        if k == len(nums):
            return nums
        
        for num in nums:
            counts[num] += 1
        
        for num in counts.keys():
            heapq.heappush(heap, (counts[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        
        

        