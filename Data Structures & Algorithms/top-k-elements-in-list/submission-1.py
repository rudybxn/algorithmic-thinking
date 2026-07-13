class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import Counter

        d = Counter(nums)
        
        heap = []
        for key,v in d.items():
            heapq.heappush(heap, (-v,key))
        res = []
        while k>0:
            val,key = heapq.heappop(heap)
            res.append(key)
            k-=1
        
        return res



