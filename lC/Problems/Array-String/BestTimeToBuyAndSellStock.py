# create folders with a file for code and a file for description



def maxProfit(self, prices):
        n = len(prices)
        lowest = prices[0]
        n = len(prices)
        maxProfit = 0
        for i in range(n):
            if prices[i] < lowest:
                lowest = prices[i]
            else:
                maxProfit = max(maxProfit, prices[i] - lowest)
        return maxProfit