class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        maxProfit = 0
        lowestPrice = prices[0]
        n = len(prices)
        for i in range(1,n):
            if prices[i] < lowestPrice:
                lowestPrice = prices[i]
            else:
                maxProfit = max(maxProfit, prices[i] - lowestPrice)   
        return maxProfit