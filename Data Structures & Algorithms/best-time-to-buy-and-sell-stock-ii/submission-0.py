class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dp(idx, canbuy):

            if idx>=len(prices):
                return 0

            if (idx, canbuy) in memo:
                return memo[(idx,canbuy)]

            skip = dp(idx+1, canbuy)
            if canbuy:
                buy = -prices[idx] + dp(idx+1, False)
                memo[(idx, canbuy)] = max(buy, skip)
            else:
                sell = prices[idx] + dp(idx+1, True)
                memo[(idx, canbuy)] = max(sell, skip)

            return memo[(idx, canbuy)]

        return dp(0, True)