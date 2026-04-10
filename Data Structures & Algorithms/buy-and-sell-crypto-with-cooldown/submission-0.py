class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        buy1,sell1=0,0
        buy2=0
        for i in range(n-1,-1,-1):
            buy=max(sell1-prices[i],buy1)
            sell=max(buy2+prices[i],sell1)
            buy2=buy1
            buy1,sell1=buy,sell
        return buy1