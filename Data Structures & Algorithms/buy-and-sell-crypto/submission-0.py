class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyp = float('inf')
        res = 0

        for p in prices:
            if p<buyp:
                buyp = p
            else:
                res = max(res,p-buyp)

        return res