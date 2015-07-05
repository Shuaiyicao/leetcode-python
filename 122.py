class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        n = len(prices)
        if n < 2:
            return 0
            
        res = 0
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
                
        return res