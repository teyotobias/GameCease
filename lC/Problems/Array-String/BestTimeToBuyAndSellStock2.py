
def maxProfit(self, prices):
        maxProfit = 0
        n = len(prices)
        for i in range(0, n-1):
            if prices[i] < prices[i+1]:
                maxProfit += (prices[i+1] - prices[i])
        return maxProfit