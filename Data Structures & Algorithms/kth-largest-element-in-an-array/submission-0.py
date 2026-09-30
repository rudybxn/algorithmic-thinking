class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []
        for n in nums:
            heapq.heappush(heap, -n)
        val = 0
        while k>0:
            val = heapq.heappop(heap)
            k-=1
        return -val
